#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to change GPS velocity respect to a selected GPS station
Only tranform Ve & Vn, will generate a new reformatted file

By Yuexin Li
"""

import math

# Parameter space
# Now the fdir and fname are hardcoded, will make it a input variable  
ref_sta="P252" #reference station
fname="pbo.nam08.vel.formatted" #reformatted velocity file
fsar="vel.xyz"
fsar_out="vel."+ref_sta+".xyz"
ref_selection='average' 
# reference pixel selection scheme:
# 'nearst': choose the nearest sar pixel to GPS as reference point
# 'average': choose the reference value as the average in a 0.1*0.1 degree box



def get_distance(lat_1, lng_1, lat_2, lng_2): 
    d_lat = lat_2 - lat_1
    d_lng = lng_2 - lng_1 

    temp = (  
         math.sin(d_lat / 2) ** 2 
       + math.cos(lat_1) 
       * math.cos(lat_2) 
       * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))



# Formatted velocity file: Lon/Lat/Ve/Vn/Name
# read vel files get reference point data
f=open(fname,'r')
data=list()
for line in f:
    data.append(line)
    if line[-5:-1]==ref_sta:
        ref_info=line.split()
        print("Choose reference station "+ref_sta)
        print("Ref lon/lat:",ref_info[0],'/',ref_info[1])
        
f.close()

# Open sar file, find the nearest point 
f1=open(fsar,'r')
lines=f1.readlines()
f1.close()
index_nearest=1
dist_min=99999999999

if ref_selection == 'nearest':
    for i in range(len(lines)):
        line=lines[i]
        line=line.split()
        dist=get_distance(float(ref_info[1]),float(ref_info[0]),float(line[1]),float(line[0]))
        if dist < dist_min:
            index_nearest=i
            dist_min=dist


    ref_line=lines[index_nearest]
    print("The nearest point is ",ref_line,index_nearest)
    print("The minimum distance is ",dist_min)

elif ref_selection == 'average':
    los_in=list()
    for i in range(len(lines)):
        line=lines[i]
        line=line.split()
        if (float(ref_info[1])-0.05 < float(line[1]) < float(ref_info[1])+0.05) and \
                     (float(ref_info[0])-0.05 < float(line[0]) < float(ref_info[0])+0.05):
             los_in.append(float(line[2]))


    ref_line=line
    ref_line[0]=ref_info[0]; ref_line[1]=ref_info[1];
    ref_line[2]=sum(los_in)/len(los_in)
    print("The average reference los value is ", ref_line[2])


#Write new files based on the nearest reference point
f2=open(fsar_out,'w')
for i in range(len(lines)):
    this_line=lines[i]
    this_line=this_line.split()
    new_line=this_line[0]+"\t"+this_line[1]+"\t"+str(float(this_line[2])-float(ref_line[2]))+"\n"
    f2.write(new_line)

f2.close()    



