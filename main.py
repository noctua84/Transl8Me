"""Main routine for the Transl8Me bot."""
import json
import platform
import sys
import os
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from core.daemon import Daemon
from core.connect import Connect

# load config and activate sentry if set.
with open("config.json") as config_file:
    config = json.load(config_file)

if config is not None:
    DSN = config["global_settings"]["sentry_dsn"]
else:
    DSN = ""

# sentry
sentry_sdk.init(
    DSN,
    traces_sample_rate=1.0,
    integrations=[AioHttpIntegration()],
    max_breadcrumbs=50,
    debug=False,
    send_default_pii=True,
    release="transl8me@2.0.0",
    environment="production",
)

con = Connect(config)


# set up deamon class:
class BotDaemon(Daemon):
    """Actual Daemon overwriting its parent run-method."""
    def run(self):
        """Override of the daemon function."""
        con.connect_bot()


if __name__ == "__main__":
    cur_os = platform.system()
    cur_env = config["global_settings"]["env"]
    cur_pid = os.getpid()
    print(cur_pid)

    if cur_os == "Linux":
        if cur_env == "dev":
            con.connect_bot()
        else:
            pid_file = config["global_settings"]["pid_file"]
            daemon = BotDaemon(pid_file)
            if len(sys.argv) == 2:
                if sys.argv[1] == "start":
                    daemon.start()
                elif sys.argv[1] == "stop":
                    daemon.stop()
                elif sys.argv[1] == "restart":
                    daemon.restart()
                else:
                    print("Unknown command")
                    sys.exit(2)
                sys.exit(0)
            else:
                print("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)

    elif cur_os == "Windows":
        # bot
        con.connect_bot()

    else:
        print("could not recognize OS")
