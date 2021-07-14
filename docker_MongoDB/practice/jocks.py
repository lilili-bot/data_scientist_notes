import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

joke = pyjokes.get_joke()

data = {'text': joke}
requests.post(url=webhook_url, json = data)
