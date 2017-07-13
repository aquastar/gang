import cPickle as pk

twitter_dict = pk.load(open('twitter.pk', 'rb'))

for _ in twitter_dict:
    print _
