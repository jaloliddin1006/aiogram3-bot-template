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