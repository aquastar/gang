from twython import Twython, TwythonError

APP_KEY = 'fLJp19pT8o5Sm4fZCNHTyuk3C'
APP_SECRET = 'PpakU3N40OMTUkPd80y2llHo6nKU4VZdMEqQwpU21mHPoEIuUH'
OAUTH_TOKEN = '18015823-iRkCqjF61NHFanjHHR4LSTqW9DSghgeBFnytAaxcu'
OAUTH_TOKEN_SECRET = '1UQNtR8IrxHY8JrdH5OwwtsBDWOtfADjn3muG9c2hSE7k'
# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    search_results = twitter.search(q='#GDK', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
