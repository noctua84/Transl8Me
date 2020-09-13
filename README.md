[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/noctua84/Transl8Me/?ref=repository-badge)  
[![CodeFactor](https://www.codefactor.io/repository/github/noctua84/transl8me/badge)](https://www.codefactor.io/repository/github/noctua84/transl8me)
![CodeInspector](https://www.code-inspector.com/project/12992/status/svg)
![CodeInspector](https://www.code-inspector.com/project/12992/score/svg)  
![Python application](https://github.com/noctua84/Transl8Me/workflows/Python%20application/badge.svg)
![Pylint](https://github.com/noctua84/Transl8Me/workflows/Pylint/badge.svg?branch=master)


## Transl8Me

Discord-Bot to translate incoming messages.  
Once started, the Bot simply translates every incoming message from english into german
and from german to english.  
Frensh translation is also possible as a third language.  
  
Other languages are currently not supported.

### Bot-Commands:

```
$help: shows help
$start: starts translation
$stop: stops translation
$status: show if bot is translating or not.
```

### Link to invite the bot:

If you want to invite the Bot to your server, just copy the link, follow the steps and your are fine.  
If you want to host the Bot on your own server follow the steps described under **Setup**

```
https://discord.com/api/oauth2/authorize?client_id=750027210772971543&permissions=11264&scope=bot
```

### Setup

To host the bot on your own server, follow the steps below.

**Important**  
To run unattended as a service, a Linux-Setup is required!  
_Tested with Ubuntu Server 20.04_

```
1. clone the repository with your preferred git-client or git-cli
2. Check if python3 and pip are installed.
3. run pip3 -r requirements.txt
4. change config_example.json to config.json
5. modify config-settings
```

### Control the service

The following commands will only work in a Linux-Environment!  
Please keep this in mind.
The Bot will run as daemon under linux and will continue running even if the console is closed.

```
1. (sudo) python3 main.py start - this will start the daemon and therefore the bot.
2. (sudo) python3 main.py stop - this will stop the daemon.
3. (sudo) python3 main.py restart - this will restart the daemon.
```
