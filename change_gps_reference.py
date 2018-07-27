#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to change GPS velocity respect to a selected GPS station
Only tranform Ve & Vn, will generate a new reformatted file

By Yuexin Li
"""

# Now the fdir and fname are hardcoded, will make it a input variable  

ref_sta="P252" #reference station
fname="pbo.nam08.vel.formatted" #reformatted velocity file
fout="pbo."+ref_sta+".vel.reformatted"

# Formatted velocity file: Lon/Lat/Ve/Vn/Name
# read vel files
f=open(fname,'r')
data=list()
for line in f:
    data.append(line)
    if line[-5:-1]==ref_sta:
        ref_info=line.split()
        print("Choose reference station "+ref_sta)
        print("Ref lon/lat:",ref_info[0],'/',ref_info[1])
f.close()

# Writing new file
fnew=open(fout,'w')
print(len(data)," lines to write...")
for i in range(len(data)):
    this_line=data[i]
    this_line=this_line.split()
    new_line=this_line[0]+"\t"+this_line[1]+"\t"+str(float(this_line[2])-float(ref_info[2]))+"\t"+str(float(this_line[3])-float(ref_info[3]))+"\t"+this_line[4]+"\n"
    fnew.write(new_line)

fnew.close()    
        
    
