"""Main routine for the Transl8Me bot."""
import json
import platform
import sys
import os
import sentry_sdk
from discord import LoginFailure
from sentry_sdk import capture_exception
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from core.bot import Bot
from core.daemon import Daemon

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


# set up deamon class:
class BotDaemon(Daemon):
    """Actual Daemon overwriting its parent run-method"""

    def run(self):
        try:
            d_token = config["global_settings"]["bot_token"]
            daemon_client = Bot(config)
            daemon_client.set_client(daemon_client)
            daemon_client.run(d_token)
        except TypeError as type_exception_daemon:
            # should not occur - just for reference
            capture_exception(type_exception_daemon)
        except LoginFailure as bot_token_exception_daemon:
            # is raised if bot-token is wrong or missing
            capture_exception(bot_token_exception_daemon)


if __name__ == "__main__":
    cur_os = platform.system()
    cur_pid = os.getpid()
    print(cur_pid)

    if cur_os == "Linux":
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
        try:
            token = config["global_settings"]["bot_token"]
            client = Bot(config)
            client.set_client(client)
            # client.loop.create_task(client.save_msg_stats())
            client.run(token)
        except TypeError as type_exception:
            capture_exception(type_exception)
        except LoginFailure as bot_token_exception:
            capture_exception(bot_token_exception)

    else:
        print("could not recognize OS")
