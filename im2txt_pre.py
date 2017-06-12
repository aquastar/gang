import glob

dir='/home/danny/Downloads/im2txt_2016_10_11.2000000/test/' + '*'

print ','.join(glob.glob(dir))