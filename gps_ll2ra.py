#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to transfer selected lon/lat into r/a radar coordinates
Used for comparing GPS and InSAR time series 

By Yuexin Li
"""

import numpy as np

gps_file="pbo.P252.vel.reformatted"
tran_file="trans.dat"
box_size=0.1 #degree


# randon lon/lat for testing
# in real case, should read in a GPS velocity file and extract these.
ref_lon=-121.8
ref_lat=37.3

# read trans.dat
# need to confirm if we read it correctly
f_trans=open(tran_file,'rb')
trans_array=np.fromfile(f_trans,np.int16).reshape((-1,5))
f_trans.close()

# read gps file
# only match the format for pbo
f_gps=open(gps_file,'r')

# for a more efficient way
# should only read trans.dat once (or line by line)
# but loop over each station 




