import http.client
import json

c = http.client.HTTPConnection('search.twitter.com')
c.request('GET','/search.json?q=pluralsight')
r = c.getresponse()
data = r.read()
datas = str(data, 'utf-8')
o = json.loads(datas)
tweets = o['results']
for tweet in tweets:
    print (tweet['text'])
    
