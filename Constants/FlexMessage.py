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
        "height": "md",
        "action": {
          "type": "postback",
          "label": "know",
          "data": "know"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "don't know",
          "data": "dont know"
        },
        "style": "primary",
        "height": "md"
      }
    ],
    "flex": 0
  }
}
    return flex

