# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:38:12 2019

@author: chenyu
"""

import os


dir_path='F:\\chenyu\\VC_DNN\\VC\\_DTW_王_周\\remove_version\\Source' #base folder

for fn in os.listdir(dir_path):
    new_name=str(fn)+'_re'
    os.rename(dir_path+'\\'+str(fn),dir_path+'\\'+str(new_name))
    #print(fn)