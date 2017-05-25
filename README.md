# Get Embed Tweet
This is exchange tweet url to embed tweet string

## require
* http server (ex. apache)
* cgi executer (ex. apache mod_cgi)
* python3.x

## install
put get_tweet.html into http accessible directory.
put get_tweet.py into http executable directory.

if get_tweet.html and get_tweet.py is not same directory.
change get_tweet.hml "var get_tweet=/path/to/get_tweet.py"

## limitation
get_tweet.html and get_tweet.py must hosted by same host.

## usage
1. open get_tweet.html
1. put tweet url into first box
1. push generate button
1. generated string into second box

