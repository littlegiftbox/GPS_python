#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to read pbo velocity file and reformat it for gmt/matlab use
Optional: only extract GPS stations in a certain region 

By Yuexin Li
"""

######### Parameter setting ###########
# Now the fdir and fname are hardcoded, will make it a input variable  
# Where your data lives
fdir="/Users/mac/data/GPS/unavco/velocity"
fname="pbo.final_nam08.vel"
# Output file in current directory
fname_out="pbo.nam08.vel.formatted"


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-R','--range',help='select your lon1 lon2 lat1 lat2 range',type=str) #somehow '/' doesn't work
args = parser.parse_args()

if args.range:
    loc_info=args.range
    loc_info=loc_info.split()
    print("Selected range is ",loc_info)
else:
    print("No region specified, will use the whole region.")


#initialization
document=list()
data=list()
file=open(fdir+'/'+fname,'r')
document_flag=0
data_flag=0
for line in open(fdir+'/'+fname,'r'):
    
    #line=file.readline()
    if data_flag==1:
        data.append(line)
        
    if document_flag==1:
        document.append(line)
    
    if line  == "Start Field Description":
        document_flag=1;
        print("start reading documentation")
        
    if line == "End Field Description":
        document_flag=0;
        print("end reading documentation")
        
    if line[0] == '*':
        data_head=line        
        data_flag=1;

file.close()

data_head=data_head.split()
# Find the column index of horizontal velocity 
# grep all the head names you need
indx_name=data_head.index('*Dot#')
indx_vn=data_head.index('dN/dt')
indx_ve=data_head.index('dE/dt')
indx_refnlat=data_head.index('Ref_Nlat')
indx_refelon=data_head.index('Ref_Elong')

# Write new output files
newfile=open(fname_out,'w')
for i in range(1,len(data)):
    this_line=data[i]
    this_line=this_line.split()
    if args.range:
        if (float(this_line[indx_refelon]) > float(loc_info[0]) and float(this_line[indx_refelon]) < float(loc_info[1]) and 
            float(this_line[indx_refnlat]) > float(loc_info[2]) and float(this_line[indx_refnlat]) < float(loc_info[3])):
            line=this_line[indx_refelon]+" "+this_line[indx_refnlat]+" "+this_line[indx_ve]+" "+this_line[indx_vn]+" "+this_line[indx_name]+"\n"
            newfile.write(line)
    else:
         line=this_line[indx_refelon]+" "+this_line[indx_refnlat]+" "+this_line[indx_ve]+" "+this_line[indx_vn]+" "+this_line[indx_name]+"\n"
         newfile.write(line)


newfile.close()

    

    
        
        
    
