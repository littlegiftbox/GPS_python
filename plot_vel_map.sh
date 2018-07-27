#!/bin/bash

# Sample scripts to practice drawing velocity maps
# Yuexin Li
# 07/12/2018


#North America Region
R=-123/-119.5/36/38
J=M15c
ps=vel_map.ps
vfile=pbo.P252.vel.reformatted
#vfile=pbo.nam08.vel.formatted
#vfile=midas.NA12.vel.formatted
sarfile=vel_180709_ll.grd
sarxyz=vel.xyz
cptfile=vel_180709_ll.cpt

gmt psbasemap -R$R -J$J -P -Bx1 -By1 -BNEWS -K -Y18 > $ps
gmt pscoast -R$R -J$J -Ggray95 -S83/216/238 -A5000 -Dh -K -O >> $ps
gmt grdimage $sarfile -R -J -C$cptfile -K -O -Q >> $ps

# Draw GPS velocities
gmt psvelo $vfile -R -J -Se10.0c/0.95/0 -A5.00c+e+p0.75p -Gblue -W0.3p,blue -K -O >> $ps
# Plot reference vel point
gmt psxy -R -J -Sc0.1 -Gblue -K -O << EOF >> $ps
238.9422695629  37.1695565340
EOF

# convert vel.grd into vel.xyz
# -s suppress NaNs
# gmt grd2xyz $sarfile -s > $sarxyz 
gmt project $sarxyz -C-122/36.5 -E-121/36.8 -Fxyzp -W-0.25/0.25 -Q > profile.tmp
gmt psxy -R -J -K -O -W1p,red << EOF >> $ps
-122 36.5
-121 36.8
EOF

gmt project $sarxyz -C-121.7/36.35 -E-120.7/36.65 -Fxyzp -W-0.25/0.25 -Q >profile.tmp2
gmt psxy -R -J -K -O -W1p,orange << EOF >> $ps
-121.7 36.35
-120.7 36.65
EOF


gmt psbasemap -R0/120/-40/40 -JX15c/5c -P -Bf2.5a10:"Distance (km)":/f10a20:"LOS velocity (mm/yr)":WS -K -O -X0 -Y-7 >> $ps  
awk '{print $4, $3, $3}' profile.tmp | gmt psxy -R -J -Sc0.1 -C$cptfile -W0.25p -P -O -K >> $ps

# -C start point 
# -E end point
# -F x,y,z,parrallel-distance-from-center,perp-dist-from-center,...

gmt psbasemap -R0/120/-40/40 -JX15c/5c -P -Bf2.5a10:"Distance (km)":/f10a20:"LOS velocity (mm/yr)":WS -K -O -X0 -Y-7 >> $ps
awk '{print $4,$3,$3}' profile.tmp2 | gmt psxy -R -J -Sc0.1 -C$cptfile -W0.25p -P -O -K >> $ps

rm profile.tmp*
rm gmt.history
open $ps
