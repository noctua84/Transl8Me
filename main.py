import json
import platform
import sys
import os
import sentry_sdk
from bot import Bot
from daemon import Daemon
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

# load config and activate sentry if set.
with open('config.json') as config_file:
    config = json.load(config_file)

if config is not None:
    DSN = config.get('sentry_dsn')
else:
    DSN = ""

# sentry
sentry_sdk.init(
    DSN,
    traces_sample_rate=1.0,
    integrations=[AioHttpIntegration()],
    release="Transl8Me@1.0.0"
)


# set up deamon class:
class BotDaemon(Daemon):
    """Actual Daemon overwriting its parent run-method"""

    def run(self):
        daemon_client = Bot()
        daemon_client.set_client(daemon_client)
        daemon_client.run(config.get("bot_token"))


if __name__ == "__main__":
    cur_os = platform.system()
    cur_pid = os.getpid()
    print(cur_pid)

    if cur_os == "Linux":
        daemon = BotDaemon('/tmp/transl8me.pid')
        if len(sys.argv) == 2:
            if 'start' == sys.argv[1]:
                daemon.start()
            elif 'stop' == sys.argv[1]:
                daemon.stop()
            elif 'restart' == sys.argv[1]:
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
        client = Bot()
        client.set_client(client)
        client.run(config.get("bot_token"))

    else:
        print("could not recognize OS")
