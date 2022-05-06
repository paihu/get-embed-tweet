import urllib.request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
import json

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def root():
    try:
        return open("get_tweet.html","r").read()
    except:
        return HTMLResponse(content="internal error",status_code=500)

@app.get('/get_tweet', response_class=PlainTextResponse)
def get_tweet(url: str = ''):
    if url.find("/photo") != -1:
        url = url[:url.find("/photo")]
    with urllib.request.urlopen('https://publish.twitter.com/oembed?url=' + url) as response:
        return response.read().decode()

