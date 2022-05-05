import urllib.request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
import json

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def root():
    return '''
    <html>
    <head>
    <title>Make Embed Tweet</title>
    <script type="text/javascript">
    var get_tweet="get_tweet";
    window.addEventListener("load",function(){
        console.log("add event listender");
        document.getElementById("generate").addEventListener("click",function(){
            console.log("generate");
            var urls = document.getElementById("in-url").value.split("\\n");
            var out = new Array(urls.length);
            urls.forEach(function(element, index, array){
                var req = new XMLHttpRequest();
                req.overrideMimeType('text/plain');
                req.responseType = "text";
                req.onreadystatechange = function() {
                    console.log("state change");
                    if (req.readyState == 4){
                        if (req.status == 200){
                            console.log(req.response);
                            out[index] = JSON.parse(req.response).html;
                            document.getElementById("out-embed").value = out.join("\\n");
                        }
                    }
                };
                req.open('GET',get_tweet + "?url=" + element, true);
                req.send(null);
            });
        },false);
    },false);
    </script>
    </head>
    
    <body>
    <textarea id="in-url" rows=10 cols=60></textarea><br>
    <button id="generate">generate</button><br>
    <textarea id="out-embed" rows=10 cols=100></textarea>
    
    </body>
    </html>
    '''

@app.get('/get_tweet', response_class=PlainTextResponse)
def get_tweet(url: str = ''):
    if url.find("/photo") != -1:
        url = url[:url.find("/photo")]
    with urllib.request.urlopen('https://publish.twitter.com/oembed?url=' + url) as response:
        return response.read().decode()
