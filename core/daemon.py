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
            sys.stderr.write(f"fork #1 failed: {err}\n")
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
            sys.stderr.write(f"fork #2 failed: {err}\n")
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
        self.__check_pid()

        # Start the daemon
        self.daemonize()
        self.run()
        print("Process started")

    def stop(self):
        """Stop the daemon."""
        # Get the pid from the pidfile and kill the process:
        self.__kill_process(self.__check_pid())
        print("Process stopped")

    def restart(self):
        """Restart the daemon."""
        self.stop()
        self.start()
        print("Process restarted")

    def run(self):
        """This method has to be overridden in specific daemon-class
        inheriting from this"""

    def __check_pid(self):
        """internal method to check if pid exists"""
        try:
            with open(self.pidfile, "r") as pid_file:
                pid = int(pid_file.read().strip())
        except IOError:
            pid = None

        if pid:
            message = f"pidfile {self.pidfile} already exist. Daemon already running?\n"
            sys.stderr.write(message)
            sys.exit(1)
        else:
            message = f"pidfile {self.pidfile} does not exist. Daemon not running?\n"
            sys.stderr.write(message)

        return pid

    def __kill_process(self, pid):
        """internal method to kill the current running process"""
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError as err:
            error = str(err.args)
            if error.find("No such process") > 0 and os.path.exists(self.pidfile):
                os.remove(self.pidfile)
            else:
                print(str(err.args))
                sys.exit(1)
