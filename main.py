"""Main routine for the Transl8Me bot."""
import json
import platform
import sys
import os
import sentry_sdk
from discord import LoginFailure
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk import capture_exception
from bot import Bot
from daemon import Daemon

# load config and activate sentry if set.
with open("config.json") as config_file:
    config = json.load(config_file)


if config is not None:
    DSN = config.get("sentry_dsn")
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
)


# set up deamon class:
class BotDaemon(Daemon):
    """Actual Daemon overwriting its parent run-method"""

    def run(self):
        try:
            daemon_client = Bot(config)
            daemon_client.set_client(daemon_client)
            daemon_client.run(config.get("bot_token"))
        except TypeError as type_exception:
            # should not occur - just for reference
            capture_exception(type_exception)
        except LoginFailure as bot_token_exception:
            # is raised if bot-token is wrong or missing
            capture_exception(bot_token_exception)


if __name__ == "__main__":
    cur_os = platform.system()
    cur_pid = os.getpid()
    print(cur_pid)

    if cur_os == "Linux":
        daemon = BotDaemon(config.get("pid_file"))
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
            client = Bot(config)
            client.set_client(client)
            client.run(config.get("bot_token"))
        except TypeError as type_exception:
            capture_exception(type_exception)
        except LoginFailure as bot_token_exception:
            capture_exception(bot_token_exception)

    else:
        print("could not recognize OS")
