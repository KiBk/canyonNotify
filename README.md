# About

It is a python bot that will check availability of a Canyon bike for you. 
Add a link to the bike that you want. Start the bot. Run `\notify` in the bot.
It will inform you if the status of any of your tracked bikes has changed

# Installation

Install the dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 
pip3 install -r requirements.txt 
```

Optionally you can run it in venv

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 
sudo apt install python3-pip
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt 
```

Rename config.example.py to config.py, add your requested Telegram TOKEN (It is requested from 
`BotFather`) and modify the bikes that you are looking for

```bash
mv config.example.py config.py
vim config.py
```

After installation is compelte, just run the main.py

```bash
python3 main.py
```

Find your bot in Telegram and Done :)


# Telegram bot commands

- `/start`
- `/help`
- `/notify` - to start notifying you about the availability
- `/unnotify` - to stop notification
- `/set` - set time interval inbetween checks
- `/status` - to do an immediate check and return the availability


# Todo
- Add a test to see if we are online
- Add an option to add/remove bikes
- Don't need to have unique jobs per user
- Put all python in /src folder

