## Transl8Me
Discord-Bot to translate incoming messages.  
Once started, the Bot simply translates every incoming message from english into german 
and from german to english.  
Other languages are currently not supported.
### Bot-Commands:
```
$help: shows help
$start: starts translation
$stop: stops translation
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
*Tested with Ubuntu Server 20.04*  
``` 
1. clone the repository with your preferred git-client or git-cli
2. Check if python3 and pip are installed.
3. run pip3 -r requirements.txt
4. start the service.
```
