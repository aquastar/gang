import cPickle as pk
import json
import os
import traceback

import requests

img_txt_list = []
page_lmt = 300
fname = 'img_txt_list.pk'

if os.path.isfile(fname):
    img_txt_list = pk.load(open(fname, 'rb'))

print 'loaded data size:', len(img_txt_list)

query_list = [
    'drinking', 'alcohol', 'drunk party', 'booze', 'liquor', 'binge drinking', 'beer', 'whiskey', 'bar', 'neon',
    'bartender',
    'gun', 'gangster', 'firearm', 'tattoo', 'smoking', 'bitch', 'drug', 'criminal', 'victim', 'violence', 'shot'
]

for q in query_list:
    print 'Query', q
    for p in xrange(1, page_lmt):
        print 'Current page', p
        url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCv94G0_nFK2WkPM12KhCuCJxh4sAIpFSc&cx=013228809236883522378:2t1dbtee42m&q={}&searchType=image&alt=json&start={}'.format(
            q, p)

        try:
            r = requests.get(url)
            rst = json.loads(r.content)['items']

            for _ in rst:
                img_txt_list.append([_['link'], _['title']])
        except:
            print traceback.print_exc()
            break

print 'data size:', len(img_txt_list)
pk.dump(img_txt_list, open(fname, 'wb'))
