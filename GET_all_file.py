# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:27:04 2019

@author: chenyu
"""
#GET all file in the directory
from pathlib import Path

def get_all_file(input_dir):
    file=[]
    for filename in Path(input_dir).glob('**/*.wav'):
        file.append(filename)
    for f in file:
        print(f)
    
    
get_all_file('F:\\chenyu\\VC_DNN\\VC\\_DTW_王_周\\remove_version\\Test_Source')