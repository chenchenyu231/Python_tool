# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:52:05 2020

@author: spblab
"""

#Total para
import sys
import tensorflow as tf
import numpy as np
import re

f=open('tmp2.txt','w')
ckpt_fpath=r'C:\Users\spblab\Desktop\Voice_Converter_CycleGAN-stable - 複製\model\debug\GatedCNN_org20200401.ckpt'
# Open TensorFlow ckpt
reader = tf.train.NewCheckpointReader(ckpt_fpath)


f.write('Count the number of parameters in ckpt file(%s)' % ckpt_fpath)
param_map = reader.get_variable_to_shape_map()
total_count = 0
pattern=r'(.+)InstanceNorm.+'

for k, v in param_map.items():
    if 'Momentum' not in k and 'global_step' not in k:
        
        if not (re.match(pattern,k)):
            temp = np.prod(v)
            total_count += temp
            f.write(('\n%s: %s => %d' % (k, str(v), temp)))

f.write('\nTotal Param Count: %d' % total_count)
print('\nTotal Param Count: %d' % total_count)



###trainable para

# import tensorflow as tf
# meta_graph_path = r'C:\Users\spblab\Desktop\Voice_Converter_CycleGAN-stable - 複製\model\debug\GatedCNN_org20200401.ckpt.meta'
# load_mod = tf.train.import_meta_graph(meta_graph_path)

# total_parameters = 0
# for variable in tf.trainable_variables():
#     # shape is an array of tf.Dimension
#     shape = variable.get_shape()
#     print(shape)
#     print(len(shape))
#     variable_parameters = 1
#     for dim in shape:
#         print(dim)
#         variable_parameters *= dim.value
#     print(variable_parameters)
#     total_parameters += variable_parameters
# print('The total number of parameters are: ', total_parameters)