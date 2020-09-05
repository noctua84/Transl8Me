"""module docstring"""
import sys
import os
import time
from signal import SIGTERM


def daemonize(stdout='/dev/null', stderr=None, stdin='/dev/null',
              pidfile=None, startmsg='started with pid %s')
  """function to daemonize the current process"""

   # first fork:
   try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
