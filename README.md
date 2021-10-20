## Statistics
![Python application](https://github.com/noctua84/Transl8Me/workflows/Python%20application/badge.svg) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnoctua84%2FTransl8Me.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnoctua84%2FTransl8Me?ref=badge_shield)
 

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/noctua84/transl8me)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)  
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/noctua84/transl8me)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/noctua84/transl8me)  

![CodeFactor](https://www.codefactor.io/repository/github/noctua84/transl8me/badge)  

![CodeInspector](https://www.code-inspector.com/project/12992/status/svg)
![CodeInspector](https://www.code-inspector.com/project/12992/score/svg)  
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/noctua84/Transl8Me)
![Code Climate issues](https://img.shields.io/codeclimate/issues/noctua84/Transl8Me)
![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/noctua84/Transl8Me)  

![DeepSource](https://deepsource.io/gh/noctua84/Transl8Me.svg/?label=active+issues&show_trend=true)
![DeepSource](https://deepsource.io/gh/noctua84/Transl8Me.svg/?label=resolved+issues&show_trend=true)  

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/noctua84/transl8me)
![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/noctua84/transl8me/latest)
  
[![wakatime](https://wakatime.com/badge/github/noctua84/Transl8Me.svg)](https://wakatime.com/badge/github/noctua84/Transl8Me)

## Transl8Me

Discord-Bot to translate incoming messages.  
Once started, the Bot simply translates every incoming message.  
Currently supported languages:  
If invited: german, english, frensh and russian.
If selfhosted: any language desired.

Each language can be source and target of a translation.

Currently supported commands:  
help, status, start, stop and stats

### Bot-Commands (all users):

```
$help: shows help
$status: show if bot is translating or not.
```

### Bot-Commands (admin only):  
```
$start: starts the translation service
$stop: stops the translation service
$stats: shows some basic message and translation stats*
-------------------------------------------------------
* the stats are currently available as long as the bot is running.  
no other details than overall are currently possible.
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
5. modify config-settings based on your infrastructure and used tools.
```

### Settings
Below is described what can be tweeked and which tools can be integrated.  
Tools are not required for the bot to work.  
Customisations, especially those for language are required for the bot to work.

**Important**  
If no command-customisation is done, every command will be treated as allowed! 

#### Tools
```
Currently pre integrated but not initially configured tools:
1. Sentry
2. Datadog
```

#### Customizations
```
To customize the bot to your own needs, you can set language and command-restrictions via config.json-file.
1. language: supplies all languages supported for translation.*
2. commands: supplies settings for restricted commands.*|**|***
------------------------------------------------------------------------------
* the settings are intedet to be key = value.
e.g.:  
"de": "de" for language  
"start": "start" for commands

** theoreticaly every imaginable command can be added, but only supported
and therefore implemented commands will be interpreted by the bot.
Implemented commands are found within config under commands.implemented section.

*** if no command is restrictet, the bot will automatically use the commands 
mentioned in the commands.implemented section.
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


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnoctua84%2FTransl8Me.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnoctua84%2FTransl8Me?ref=badge_large)