import cPickle as pk
import json
import urllib

train_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/train2014'
val_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/val2014'
train_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_train2014.json'
val_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_val2014.json'

train_label = json.load(open(train_label_path, 'r'))
val_label = json.load(open(val_label_path, 'r'))

print('train #', len(train_label['images']), len(train_label['annotations']))
print('val #', len(val_label['images']), len(val_label['annotations']))

fname = 'img_txt_list.pk'
img_txt_list = pk.load(open(fname, 'rb'))
img_txt_len = len(img_txt_list)

img_id = 600000
tid = 900000
split_num = 5
for _id, _ in enumerate(img_txt_list):
    print '[ PROGRESS ]', _id, '-', img_txt_len,
    img_id += 1
    tid += 1

    if _id % split_num == 0:
        # download to corresponding folder, replacing 000000000094 with padded number
        filename = u'/COCO_val2014_{}.jpg'.format(str(img_id).zfill(12))
        urllib.urlretrieve(_[0], val_data_path + filename)

        # write the corresponding file
        # write val_label[u'annotations'] with image_id = max(image_id) + 1
        # write val_label[u'images'] with id = image_id
        tmp_dict = {
            u'caption': _[1].split('-')[0],
            u'id': tid,
            u'image_id': img_id
        }
        print tmp_dict['caption']
        val_label['annotations'].append(tmp_dict)
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
        val_label['images'].append(tmp_dict)


    else:
        # download to corresponding folder, replacing 000000000094 with padded number
        filename = u'/COCO_train2014_{}.jpg'.format(str(img_id).zfill(12))
        urllib.urlretrieve(_[0], val_data_path + filename)

        # write the corresponding file
        # write val_label[u'annotations'] with image_id = max(image_id) + 1
        # write val_label[u'images'] with id = image_id
        tmp_dict = {
            u'caption': _[1].split('-')[0],
            u'id': tid,
            u'image_id': img_id
        }
        print tmp_dict['caption']
        train_label['annotations'].append(tmp_dict)
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
        train_label['images'].append(tmp_dict)

print('train #', len(train_label['images']), len(train_label['annotations']))
print('val #', len(val_label['images']), len(val_label['annotations']))
json.load(train_label, open(train_label_path, 'w'))
json.load(val_label, open(val_label_path, 'w'))
