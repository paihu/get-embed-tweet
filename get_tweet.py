import urllib.request
import sys
import cgi
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if 'HTTP_REFERER' in os.environ:
    if 'HTTP_HOST' in os.environ:
        if not os.environ['HTTP_REFERER'].find(os.environ['HTTP_HOST']):
            print("Content-type: text/plain; chaeset=UTF-8\n\n referer not good")
            exit(1)
else:
    print("Content-type: text/plain; chaeset=UTF-8\n\n referer not set")
if 'QUERY_STRING' in os.environ:
    query = cgi.parse_qs(os.environ['QUERY_STRING'])
else:
    query = {}

if 'url' in query:
    url = cgi.escape(query['url'][0])
else:
    url = sys.argv[1]

if url.find("/photo") != -1:
    url = url[:url.find("/photo")]

with urllib.request.urlopen('https://publish.twitter.com/oembed?url=' + url) as response:
    print("Content-type: application/json; charset=UTF-8\n\n",response.read().decode())
