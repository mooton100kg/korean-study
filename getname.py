# -*- coding: utf-8 -*-

import os
import sys

from linebot import (
    LineBotApi,
)

from linebot.models import (
    RichMenu,
    RichMenuArea,
    RichMenuSize,
    RichMenuBounds,
    URIAction
)
from linebot.models.actions import MessageAction
from linebot.models.rich_menu import RichMenuAlias
import json
from Constants import getChannelToken
line_bot_api = LineBotApi(getChannelToken())


x = json.loads(str(line_bot_api.get_rich_menu_alias_list()))
y = json.loads(str(line_bot_api.get_rich_menu_list()))
if len(x['aliases']) > 0:
    for i in range(len(x['aliases'])):
        line_bot_api.delete_rich_menu_alias(x['aliases'][i]['richMenuAliasId'])
if len(y) > 0:
    for i in range(len(y)):
        line_bot_api.delete_rich_menu(y[i]['richMenuId'])

x = line_bot_api.get_rich_menu_alias_list()
y = line_bot_api.get_rich_menu_list()
print(x)
print(y)

