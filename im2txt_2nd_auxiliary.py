import cPickle as pk
import json
import urllib

train_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/train2014'
val_data_path = '/home/danny/models/im2txt/data/mscoco/raw-data/val2014'
train_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_train2014.json'
val_label_path = '/home/danny/models/im2txt/data/mscoco/raw-data/annotations/captions_val2014.json'

train_label = json.load(open(train_label_path, 'r'))
val_label = json.load(open(val_label_path, 'r'))

fname = 'img_txt_list.pk'
img_txt_list = pk.load(open(fname, 'rb'))

split_num = 5
for _id, _ in enumerate(img_txt_list):
    # calculate the id

    if _id % split_num == 0:
        # download to corresponding folder
        urllib.urlretrieve(_[0], val_data_path)

        # write the corresponding file
        # write val_label[u'annotations'] with image_id = max(image_id) + 1
        # write val_label[u'images'] with id = image_id
        pass
    else:
        # download to corresponding folder

        # write the corresponding file
        pass
