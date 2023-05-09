# Telegram-Login-Notification

Get a Telegram Notification when someone logs in to your Linux Computer (Server, Laptop, Desktop).


## Manual Installation

Download this repository, all needed files are in the folder /src. Open a terminal and start with: 

1) `$ cd /etc`
2) `$ sudo nano profile` (Opens a terminal editor)
3) Copy the last line from src/profile in your editor. Close the editor with Ctrl+S & Ctrl+X.
4) Copy the file src/notfier.py somewhere to your home directory. Fill in Telegram Bot Token and your chat id. Remember the path and run `$ sudo chmod +x notifier.py`
4) `$ sudo nano opt/login.sh`
5) Copy content from src/login.sh in the editor and fill in the remembered path. Close the editor with Ctrl+S & Ctrl+X and run `$ sudo chmod +x login.sh`.

## How?

1) When you log in the /etc/profile script will be executed --> It is used to set system wide environmental variables on users shells.
2) The line /opt/login.sh will be executed --> /opt is for third-party applications that don't rely on any dependencies outside the scope of packages.
3) /opt/login.sh will then execute a python script on wherever path you want. You can also place it in /opt or your home directory.
4) The python script (notifier.py) uses the package [telebot](https://pypi.org/project/pyTelegramBotAPI/) to communicate with Telegram. --> `$ pip3 install pyTelegramBotAPI`

## Problems?

- Try `$ sudo chmod +x path/to/file.sh or file.py` to make the scripts and python code executable

## Automatic Installation

Eventually I will built an installer in the future...
