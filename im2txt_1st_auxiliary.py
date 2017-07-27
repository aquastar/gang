import cPickle as pk
import json
import string
import urllib

from nltk.corpus import stopwords

train_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/train2014'
val_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/val2014'
train_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_train2014.json'
val_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_val2014.json'

train_label = json.load(open(train_label_path, 'r'))
val_label = json.load(open(val_label_path, 'r'))

print('After reading')
print('train #', len(train_label['images']), len(train_label['annotations']))
print('val #', len(val_label['images']), len(val_label['annotations']))

fname = 'img_txt_list.pk'
img_txt_list = pk.load(open(fname, 'rb'))
img_txt_len = len(img_txt_list)

# clean current caption
for _id, _ in enumerate(train_label[u'annotations']):
    train_label[u'annotations'][_id][u'caption'] = "".join(
        l for l in _[u'caption'].lower() if
        l not in string.punctuation and l not in stopwords.words('english')).strip().decode(
        'utf-8'),

for _id, _ in enumerate(val_label[u'annotations']):
    val_label[u'annotations'][_id][u'caption'] = "".join(
        l for l in _[u'caption'].lower() if
        l not in string.punctuation and l not in stopwords.words('english')).strip().decode(
        'utf-8'),

print('After cleaning')
print('train #', len(train_label['images']), len(train_label['annotations']))
print('val #', len(val_label['images']), len(val_label['annotations']))

img_id = 600000
tid = 900000
split_num = 5
for _id, _ in enumerate(img_txt_list):
    print '[ PROGRESS ]', _id, '-', img_txt_len,
    img_id += 1
    tid += 1
    tmp_dict = {}
    try:
        tmp_dict = {
            u'caption': _[1].split('-')[0].lower().replace(',', '').replace('-', '').replace('.', '').replace(
                ':', '').replace('free photo', '').replace('free vector graphic', '').replace('free illustration',
                                                                                              '').strip().decode(
                'utf-8'),
            u'id': tid,
            u'image_id': img_id
        }
    except:
        print 'Not unicode'
        continue

    if _id % split_num == 0:
        # download to corresponding folder, replacing 000000000094 with padded number
        filename = u'/COCO_val2014_{}.jpg'.format(str(img_id).zfill(12))

        try:
            urllib.urlretrieve(_[0], val_data_path + filename)
        except:
            print 'Missed link'
            continue

        print tmp_dict[u'caption']
        val_label[u'annotations'].append(tmp_dict)
        tmp_dict = {
            u'coco_url': u'http://mscoco.org/images/xxx',
            u'date_captured': u'2013-11-14 11:38:44',
            u'file_name': filename,
            u'flickr_url': u'http://farm1.staticflickr.com/1/xxx.jpg',
            u'height': 480,
            u'id': img_id,
            u'license': 3,
            u'width': 640
        }
        val_label[u'images'].append(tmp_dict)


    else:
        # download to corresponding folder, replacing 000000000094 with padded number
        filename = u'/COCO_train2014_{}.jpg'.format(str(img_id).zfill(12))

        try:
            urllib.urlretrieve(_[0], val_data_path + filename)
        except:
            print 'Missed link'
            continue

        print tmp_dict[u'caption']
        train_label[u'annotations'].append(tmp_dict)
        tmp_dict = {
            u'coco_url': u'http://mscoco.org/images/xxx',
            u'date_captured': u'2013-11-14 11:38:44',
            u'file_name': filename,
            u'flickr_url': u'http://farm1.staticflickr.com/1/xxx.jpg',
            u'height': 480,
            u'id': img_id,
            u'license': 3,
            u'width': 640
        }
        train_label[u'images'].append(tmp_dict)

print('train #', len(train_label[u'images']), len(train_label[u'annotations']))
print('val #', len(val_label[u'images']), len(val_label[u'annotations']))
json.dump(train_label, open(train_label_path, 'w'))
json.dump(val_label, open(val_label_path, 'w'))
