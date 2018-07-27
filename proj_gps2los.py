#!/usr/bin/env python3

"""
Script to project horizontal GPS velocity into LOS direction
Now only use one single look vector

By Yuexin Li
"""

ref_sta="P252"
fname="pbo."+ref_sta+".vel.reformatted"
fout="pbo."+ref_sta+".vel.los"
look_E=0.707761
look_N=-0.115223

f=open(fname,'r')
data=f.readlines()
f.close()

fnew=open(fout,'w')
for i in range(len(data)):
    this_line=data[i]
    this_line=this_line.split()
    los=str(-1000*(float(this_line[2])*look_E+float(this_line[3])*look_N))
    #los change from m/yr to mm/yr
    new_line=this_line[0]+"\t"+this_line[1]+"\t"+los+"\t"+this_line[4]+"\n"
    fnew.write(new_line)

fnew.close()
