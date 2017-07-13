from twython import Twython, TwythonError, TwythonRateLimitError
from util import twitter_accounts, hashtags
import cPickle as pk
import sys


def get_twitter_account(tid=0):
    APP_KEY = twitter_accounts[tid][0]
    APP_SECRET = twitter_accounts[tid][1]
    OAUTH_TOKEN = twitter_accounts[tid][2]
    OAUTH_TOKEN_SECRET = twitter_accounts[tid][3]
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    return twitter


if __name__ == '__main__':
    tid = 0
    twitter = get_twitter_account(tid)

    twitter_dict = []
    for h in hashtags:

        next_max_id = 0
        collected_num = 0
        while collected_num < 2000:
            search_results = []
            try:
                if next_max_id == 0:
                    search_results = twitter.search(q=h, count=50)
                else:
                    search_results = twitter.search(q=h, count=50, max_id=next_max_id)
            except TwythonError as e:
                print e
            except TwythonRateLimitError:
                print e
                if tid > len(twitter_accounts):
                    raise TwythonRateLimitError
                else:
                    twitter = get_twitter_account(tid + 1)
                    continue

            print ' - collected_num for :', h, collected_num
            if 'next_results' not in search_results['search_metadata']:
                print 'no more results for', h
                break
            next_results_url_params = search_results['search_metadata']['next_results']
            next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
            collected_num += len(search_results['statuses'])
            for tweet in search_results['statuses']:
                print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
                print tweet['text'].encode('utf-8'), '\n'
                twitter_dict.append([tweet['user'], tweet['text'].encode('utf-8')])

    print 'In Total', len(twitter_dict)
    pk.dump(twitter_dict, open('twitter.pk', 'wb'))
