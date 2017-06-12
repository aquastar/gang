#!/usr/bin/env bash

# run
# sh im2txt.sh "`python im2txt_pre.py`"

/home/danny/models/im2txt/bazel-bin/im2txt/run_inference \
--checkpoint_path=/home/danny/Downloads/im2txt_2016_10_11.2000000/model.ckpt-2000000 \
--vocab_file=/home/danny/Downloads/im2txt_2016_10_11.2000000/word_counts.txt \
--input_files=$1