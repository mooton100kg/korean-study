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
from linebot.models.actions import MessageAction, PostbackAction
from linebot.models.rich_menu import RichMenuAlias

from Constants import getChannelToken
line_bot_api = LineBotApi(getChannelToken())

def rich_menu_object_json():
    return {
        "size": {
            "width": 2500,
            "height": 1686
        },
        "selected": False,
        "name": "richmenu",
        "chatBarText": "Tap to open",
        "areas": [
            {
                "bounds": {
                    "x": 0,
                    "y": 0,
                    "width": 1250,
                    "height": 843
                },
                "action": {
                    "type": "postback",
                    "label": "flash_card",
                    "data": "flash_card"
                }
            },
            {
                "bounds": {
                    "x": 1251,
                    "y": 0,
                    "width": 1250,
                    "height": 843
                },
                "action": {
                    "type": "postback",
                    "label": "spelling",
                    "data": "spelling"
                }
            },
            {
                "bounds": {
                    "x": 0,
                    "y": 844,
                    "width": 1250,
                    "height": 843
                },
                "action": {
                    "type": "postback",
                    "label": "add_word",
                    "data": "add_word"
                }
            },
            {
                "bounds": {
                    "x": 1251,
                    "y": 844,
                    "width": 1250,
                    "height": 843
                },
                "action": {
                    "type": "uri",
                    "uri" : "https://docs.google.com/spreadsheets/d/1LtB3sGdzdls2nrckWJTGu-bj69vM-7nVqjobDNAnVNQ/edit?usp=sharing"
                }
            }
        ]
    }



def create_action(action):
    if action['type'] == 'uri':
        return URIAction(type=action['type'], uri=action.get('uri'))
    else:
        return PostbackAction(label=action['label'], data=action['data'])



def main():
    # create rich menu main
    rich_menu_object = rich_menu_object_json()
    areas = [
        RichMenuArea(
            bounds=RichMenuBounds(
                x=info['bounds']['x'],
                y=info['bounds']['y'],
                width=info['bounds']['width'],
                height=info['bounds']['height']
            ),
            action=create_action(info['action'])
        ) for info in rich_menu_object['areas']
    ]

    rich_menu_to_a_create = RichMenu(
        size=RichMenuSize(width=rich_menu_object['size']['width'], height=rich_menu_object['size']['height']),
        selected=rich_menu_object['selected'],
        name=rich_menu_object['name'],
        chat_bar_text=rich_menu_object['name'],
        areas=areas
    )

    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_a_create)

    with open('./image/richmenu.png', 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

    # 6. Set rich menu A as the default rich menu
    line_bot_api.set_default_rich_menu(rich_menu_id)

    # Create rich menu alias main
    alias = RichMenuAlias(
        rich_menu_alias_id='richmenu',
        rich_menu_id=rich_menu_id
    )
    line_bot_api.create_rich_menu_alias(alias)

    print("SYSTEM: finished")



main()
