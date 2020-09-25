"""This is a Linux-Deamon"""
import os
import sys
import atexit
import signal
import time


class Daemon:
    """A generic daemon class. Usage: subclass the daemon
    class and override the run() method."""

    def __init__(self, pidfile):
        self.pidfile = pidfile

    def daemonize(self):
        """Deamonize class. UNIX double fork mechanism."""

        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write("fork #1 failed: {0}\n".format(err))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write("fork #2 failed: {0}\n".format(err))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        stdin = open(os.devnull, "r")
        stdout = open(os.devnull, "a+")
        stderr = open(os.devnull, "a+")

        os.dup2(stdin.fileno(), sys.stdin.fileno())
        os.dup2(stdout.fileno(), sys.stdout.fileno())
        os.dup2(stderr.fileno(), sys.stderr.fileno())

        # write pid file
        atexit.register(self.delete_pid)

        pid = str(os.getpid())
        with open(self.pidfile, "w+") as file:
            file.write(pid + "\n")

    def delete_pid(self):
        """Remove the pid-file"""
        os.remove(self.pidfile)

    def start(self):
        """Start the daemon."""

        # Check for a pidfile to see if the daemon already runs
        try:
            with open(self.pidfile, "r") as pid_file:
                pid = int(pid_file.read().strip())
        except IOError:
            pid = None

        if pid:
            message = "pidfile {0} already exist. " + "Daemon already running?\n"
            sys.stderr.write(message.format(self.pidfile))
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """Stop the daemon."""

        # Get the pid from the pidfile
        try:
            with open(self.pidfile, "r") as pid_file:
                pid = int(pid_file.read().strip())
        except IOError:
            pid = None

        if not pid:
            message = "pidfile {0} does not exist. " + "Daemon not running?\n"
            sys.stderr.write(message.format(self.pidfile))
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            error = str(err.args)
            if error.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err.args))
                sys.exit(1)

    def restart(self):
        """Restart the daemon."""
        self.stop()
        self.start()

    def run(self):
        """This method has to be overridden in specific daemon-class
        inheriting from this"""
