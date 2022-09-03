def getFlexMessage():
    flex = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "one",
          "data": "hello"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "two",
          "data": "hello"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "three",
          "data": "hello"
        },
        "style": "primary"
      }
    ],
    "flex": 0
  }
}
    return flex