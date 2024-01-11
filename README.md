> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.


 # aiogram3-template-structure

```python
|- bot.py .
|- loader.py
|- callbaks
|  |- __init__.py
|  |- pagination.py
|- data
|  |- __init__.py
|  |- config_reader.py
|- filters
|  |- __init__.py
|  |- is_admin.py
|  |- is_channel.py
|  |- is_group.py
|  |- is_private_chat.py
|- handlers
|  |- __init__.py
|  |- users
|  |  |- __init__.py
|  |  |- start.py
|  |  |- commands.py
|  |- groups
|  |  |- __init__.py
|  |- channels
|  |  |- __init__.py
|- keyboards 
|  |- __init__.py
|  |- builders.py
|  |- fabrics.py
|  |- inline.py
|  |- reply.py
|- middlewares
|  |- __init__.py
|  |- antiflood.py
|  |- check_sub.py
|- utils
|  |- __init__.py
|  |- bot_start.py
|  |- set_bot_commands.py
|  |- states.py
```
#
Support  - <a href="https://t.me/Jaloliddin_Mamatmusayev">Telegram</a><br>

# Installation
* 1 - clone repo 
   - ```git clone https://github.com/jaloliddin1006/Aiogram3-template.git```
* 2 - create a virtual environment and activate
  - ```pip3 install virtualenv``` or ```virtualenv venv```
  - ```virtualenv venv```
  - ```venv\Scripts\activate```(windows) or ```source venv/bin/activate```(unix-based systems)
* 3 - cd into project ```cd Aiogram3-template```
* 4 - Install dependencies
  - ```pip3 install -r requirements.txt```
* 5 - Set your environment variables
  - ```cp .env.example .env```
* 6 - Run bot
  - ```python3 bot.py```


#
> Quidagi funksiyalari tayyor
```
 channel reqiured +
 defoult bot commands +
states +
inline btn +
reply btn +
builder btn +
pagination +
admin filter +
private chat filter +
groups filter +
channels filter +
connect db -
inline -
```

#

# DEPLOY
>systemd setting
```sh
[Unit]
Description=Aiogram bot
After=network.target

[Service]
User=root
Group=root
Type=simple
WorkingDirectory=/var/www/Aiogram3-template
ExecStart=/root/.local/bin/poetry run Aiogram3-template
EnvironmentFile=/var/www/Aiogram3-template/.env
Restart=always

[Install]
WantedBy=multi-user.target
```