#!/usr/bin/env bash

# Location to save the MSCOCO data.
MSCOCO_DIR="${HOME}/models/im2txt/data/mscoco"


# Build the script.
cd "${HOME}/models/im2txt/"
bazel build //im2txt:download_and_preprocess_mscoco

# Run the script.
bazel-bin/im2txt/download_and_preprocess_mscoco "${MSCOCO_DIR}"