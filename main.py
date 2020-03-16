from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)

from linebot.exceptions import(InvalidSignatureError)

from linebot.models import(MessageEvent, TextMessage, TextSendMessage)

import os

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["cpole8YwHA4bNQhJvIOb3/huz3HkdEogqK95nc2rxfO7xyoH4YVWyCQpavhbiW/qttQadsLmZmthLS/AjjvrsdDZUqdxbap6E1kUGEAwEE7vHssyFkzh2qo2Z9TbCb3krO1GtbxrfRvWbLFZ0dvXSAdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["d8e17a5b1d30f1ed61b43dcd0b3a0bc7"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=["post"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)

    try :
        handler.handle(body, signature)
    except InvalidSignatureError :
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    port = int(os.getenv("PORT",50000))
    app.run(host="0.0.0.0",port=port)