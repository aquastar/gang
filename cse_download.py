import urllib
import cPickle as pk

fname = 'img_txt_list.pk'
img_txt_list = pk.load(open(fname, 'rb'))

for _ in img_txt_list:
    urllib.urlretrieve(str(ent[1]), folder_path)