###############################################################################
# Copyright Kitware Inc. and Contributors
# Distributed under the Apache License, 2.0 (apache.org/licenses/LICENSE-2.0)
# See accompanying Copyright.txt and LICENSE files for details
###############################################################################

from collections import namedtuple

Config = namedtuple("Config", [
    "dataset_path",
    "pretrain_model_path",
    "out_fname",
    "folder",
    "img_rows",
    "img_cols",
    "target_rows",
    "target_cols",
    "num_channels",
    "network",
    "loss",
    "optimizer",
    "lr",
    "batch_size",
    "epoch_size",
    "nb_epoch",
    "test_batch_size",
    "test_iter_size",
    "dbg",
    "save_images",
    "test_pad",
    "train_pad",
    "results_dir",
    "iter_size"
])
