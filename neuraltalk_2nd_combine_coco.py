import cPickle as pk
import json
import os.path
import urllib

gang_js = json.load(open('neuraltalk.json', 'r'))
coco_js = json.load(open('captions_train2014.json', 'r'))

# [{ "file_path": "path/img.jpg", "captions": ["a caption", "a similar caption" ...] }, ...]

for _ in coco_js[u'annotations']:

    cap = None
    if isinstance(coco_js[u'annotations'][0][u'caption'], list):
        if all([__.strip() == '' for __ in _[u'caption']]):
            print 'Null Caption: {}'.format(_)
            continue
        cap = [___ for ___ in _[u'caption'] if ___.strip() != '']

    else:
        cap = [coco_js[u'annotations'][0][u'caption'].strip()]
        if cap[0].strip == '':
            print 'Null Caption: {}'.format(_)
            continue

    tmp_dict = {
        "file_path": 'train2014/COCO_train2014_{}.jpg'.format(str(_[u'image_id']).zfill(12)),
        "captions": cap
    }
    gang_js.append(tmp_dict)

json.dump(gang_js, open('combo.json', 'w'))

#
# img_id = 600000
# tid = 900000
# split_num = 5
# dict_list = []
# for _id, _ in enumerate(img_txt_list):
#     print '[ PROGRESS ]', _id, '-', img_txt_len,
#
#     img_id += 1
#     tid += 1
#
#     # download to corresponding folder, replacing 000000000094 with padded number
#     filename = 'img/gang_{}.jpg'.format(str(img_id).zfill(12))
#
#     if not os.path.isfile(filename):
#         try:
#             urllib.urlretrieve(_[0], filename)
#             print 'Downloading {}'.format(_[0])
#         except:
#             print 'Missed link {}'.format(_[0])
#             continue
#     else:
#         print '{} exists!'.format(filename)
#     tmp_dict = {
#         "file_path": filename.encode("utf-8"),
#         "captions": [_[1].encode("utf-8").split('-')[0].lower().replace(',', '').replace('-', '').replace('.', '').replace(
#             ':', '').replace('free photo', '').replace('free vector graphic', '').replace('free illustration',
#                                                                                           '').strip()]
#     }
#     dict_list.append(tmp_dict)
#
# print 'end'
# print('train #', len(train_label[u'images']), len(train_label[u'annotations']))
# print('val #', len(val_label[u'images']), len(val_label[u'annotations']))
# json.dump(train_label, open(train_label_path, 'w'))
# json.dump(val_label, open(val_label_path, 'w'))

# json.dump(dict_list, open('neuraltalk.json', 'w'))
