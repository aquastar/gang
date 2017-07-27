import cPickle as pk
import json
import os.path
import urllib

train_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/train2014'
val_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/val2014'
train_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_train2014.json'
val_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_val2014.json'

# train_label = json.load(open(train_label_path, 'r'))
# val_label = json.load(open(val_label_path, 'r'))
#
# print('After reading')
# print('train #', len(train_label['images']), len(train_label['annotations']))
# print('val #', len(val_label['images']), len(val_label['annotations']))

fname = 'img_txt_list.pk'
img_txt_list = pk.load(open(fname, 'rb'))
img_txt_len = len(img_txt_list)

# [{ "file_path": "path/img.jpg", "captions": ["a caption", "a similar caption" ...] }, ...]

img_id = 600000
tid = 900000
split_num = 5
dict_list = []
for _id, _ in enumerate(img_txt_list):
    print '[ PROGRESS ]', _id, '-', img_txt_len,

    img_id += 1
    tid += 1

    # download to corresponding folder, replacing 000000000094 with padded number
    filename = 'img/gang_{}.jpg'.format(str(img_id).zfill(12))

    if not os.path.isfile(filename):
        try:
            urllib.urlretrieve(_[0], filename)
            print 'Downloading {}'.format(_[0])
        except:
            print 'Missed link {}'.format(_[0])
            continue
    else:
        print '{} exists!'.format(filename)
    tmp_dict = {
        "file_path": filename.encode("utf-8"),
        "captions": [_[1].encode("utf-8").split('-')[0].lower().replace(',', '').replace('-', '').replace('.', '').replace(
            ':', '').replace('free photo', '').replace('free vector graphic', '').replace('free illustration',
                                                                                          '').strip()]
    }
    dict_list.append(tmp_dict)

print 'end'
# print('train #', len(train_label[u'images']), len(train_label[u'annotations']))
# print('val #', len(val_label[u'images']), len(val_label[u'annotations']))
# json.dump(train_label, open(train_label_path, 'w'))
# json.dump(val_label, open(val_label_path, 'w'))

json.dump(dict_list, open('neuraltalk.json', 'w'))
