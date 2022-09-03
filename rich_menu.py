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

from Constants import getChannelToken

line_bot_api = LineBotApi("A/LutxhuQ5rBx5XTmfo5CyEZA4ov5ijZ7L7KuVzhLEHEVYIvnJV8+XAbvnUtjWfvu60ilWdfR6abusJkuLBNA4TDOGBN1OnSK+qkMTZf8ZzGi3m0oBy5kOzOS6CTc8fZ5mTUULWfWuP39dYo6NynqQdB04t89/1O/w1cDnyilFU=")

def rich_menu_object_a_json():
    return {
        "size": {
            "width": 2500,
            "height": 1686
        },
        "selected": False,
        "name": "richmenu-a",
        "chatBarText": "Tap to open",
        "areas": [
            {
                "bounds": {
                    "x": 0,
                    "y": 0,
                    "width": 1250,
                    "height": 1686
                },
                "action": {
                    "type": "uri",
                    "uri": "https://www.line-community.me/"
                }
            },
            {
                "bounds": {
                    "x": 1251,
                    "y": 0,
                    "width": 1250,
                    "height": 1686
                },
                "action": {
                    "type": "uri",
                    "uri": "https://www.line-community.me/"
                }
            }
        ]
    }


def create_action(action):
    if action['type'] == 'uri':
        return URIAction(type=action['type'], uri=action.get('uri'))


def main():
    # 2. Create rich menu A (richmenu-a)
    rich_menu_object_a = rich_menu_object_a_json()
    areas = [
        RichMenuArea(
            bounds=RichMenuBounds(
                x=info['bounds']['x'],
                y=info['bounds']['y'],
                width=info['bounds']['width'],
                height=info['bounds']['height']
            ),
            action=create_action(info['action'])
        ) for info in rich_menu_object_a['areas']
    ]

    rich_menu_to_a_create = RichMenu(
        size=RichMenuSize(width=rich_menu_object_a['size']['width'], height=rich_menu_object_a['size']['height']),
        selected=rich_menu_object_a['selected'],
        name=rich_menu_object_a['name'],
        chat_bar_text=rich_menu_object_a['name'],
        areas=areas
    )

    rich_menu_a_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_a_create)

    # 3. Upload image to rich menu A
    with open('./image/richmenu-b.png', 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_a_id, 'image/png', f)

    # 6. Set rich menu A as the default rich menu
    line_bot_api.set_default_rich_menu(rich_menu_a_id)

    # 7. Create rich menu alias A
    alias_a = RichMenuAlias(
        rich_menu_alias_id='richmenu-nggew',
        rich_menu_id=rich_menu_a_id
    )
    line_bot_api.create_rich_menu_alias(alias_a)

    print('success')


main()
