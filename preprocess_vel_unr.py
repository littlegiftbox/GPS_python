#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to read unr GPS velocity file and reformat it for gmt/matlab use
Need to grab station location in llh file

By Yuexin Li
"""

# Now the fdir and fname are hardcoded, will make it a input variable  
# Where your data lives
fdir="/Users/mac/data/GPS/UNR"
fname="midas.NA12.txt"
fsta="llh" #station location filename
fout="midas.NA12.vel.formatted" #output filename
fout_bad="midas.NA12.vel.formatted.badpoints" #output filename
# In UNR concention velocity files:
# column 1: Station name
# column 9-11: East, north, up mode velocities (m/yr)
# column 12-14: East, north, up mode velocity uncertainties (m/yr)

# In UNR location files:
# column 1: Station name
# column 2: Latitude
# column 3: Longitude

# First read in station location files 
sta_file=open(fdir+'/'+fsta,'r')
sta_dict={}
for line in open(fdir+'/'+fsta,'r'):
    line=line.split()
    sta_dict[line[0]] = {'lon':line[2],'lat':line[1]}

sta_file.close()

"""
sta_dict={}
sta_dict = {'sta1':{'lon':, 'lat':}, ...}
sta_dict['sta_name']['lon'/'lat']
if 'sta_x' in sta_dict --> True/False
sta_dict['sta_x']={}

f = open(file_name); lines = f.readlines(); f.close()


"""

# Then read in GPS velocity files
vel_file=open(fdir+'/'+fname,'r')
vel=[]
for line in vel_file:
    vel.append(line)
vel_file.close()
    

# Write new output files
newfile=open(fout,'w')
badfile=open(fout_bad,'w')
for i in range(1,len(vel)):
    this_line=vel[i]
    this_line=this_line.split()
    sta_name=this_line[0]
    # index 9~11 should be 8~10 in Python convention
    line=sta_dict[sta_name]['lon']+" "+sta_dict[sta_name]['lat']+" "+this_line[8]+" "+this_line[9]+" "+sta_name+"\n"
    if float(this_line[8]) < 1 and float(this_line[9]) <1:
        newfile.write(line)
    else:
        badfile.write(line)

newfile.close()
badfile.close()
    

    
        
        
    
