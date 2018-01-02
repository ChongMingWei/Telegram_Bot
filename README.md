# TOC Project Telegram Bot 

##Description

This is a bot who can search all professors in NCKU CSIE for you

##Structure

1.Four states,including "start","state1","state2","state3"

2.When you type 'a',you'll enter in state1,it will reply the professors in inst.CSIE,then go back to start and wait for another type.

3.When you type 'b',you'll enter in state2,it will reply the professors in IMI,then go back to start and wait for another type.

4.When you type 'c',you'll enter in state3,it will reply the professors in IMIS,then go back to start and wait for another type.

##Run

1.Open the cmd and get into the folder includeing ngrok.exe.

2.Type 'ngrok http 5000' on the cmd.

```sh
ngrok http 5000
```

3.Change the URL in app.py and then excecute it on python IDLE.

4.Interacting with the bot.