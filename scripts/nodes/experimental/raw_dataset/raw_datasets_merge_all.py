#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from roars.rosutils.rosnode import RosNode
from roars.vision.cameras import CameraRGB
from roars.vision.arucoutils import MarkerDetector
from roars.vision.arp import ARP
from roars.vision.augmentereality import BoundingBoxFromSixPoints, VirtualObject
from roars.datasets.datasetutils import RawDataset
import roars.geometry.transformations as transformations
from collections import OrderedDict
import roars.vision.cvutils as cvutils
import cv2
import numpy as np
import os
import glob
import sys
import shutil

#⬢⬢⬢⬢⬢➤ NODE
node = RosNode("raw_datasets_merge_all")

datasets_folder = node.setupParameter("datasets_folder", "")
output_folder = node.setupParameter("output_folder", "")

raw_dataset_folders = sorted(os.listdir(datasets_folder))


data_list = []
#⬢⬢⬢⬢⬢➤ Groups all data
whole_data = {}
for d in raw_dataset_folders:
    dataset_path = os.path.join(datasets_folder, d)
    dataset = RawDataset(dataset_path)
    data_list.extend(dataset.data_list)


dataset = RawDataset(output_folder, create=True)

ZERO_PADDING_SIZE = 5
counter = 0
for data in data_list:

    counter_string = '{}'.format(str(counter).zfill(ZERO_PADDING_SIZE))

    img_file = os.path.join(dataset.img_folder, counter_string + ".jpg")
    label_file = os.path.join(dataset.label_folder, counter_string + ".txt")
    id_file = os.path.join(dataset.ids_folder, counter_string + ".txt")

    shutil.copyfile(data['image'], img_file)
    shutil.copyfile(data['id'], id_file)
    shutil.copyfile(data['label'], label_file)

    print data['id']

    counter = counter + 1
