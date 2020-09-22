#
# Undirected graph - in-degree Distribution. G(3213, 115664). 489 (0.1522) nodes with in-deg > avg deg (72.0), 88 (0.0274) with >2*avg.deg (Mon Sep 21 20:56:12 2020)
#

set title "Undirected graph - in-degree Distribution. G(3213, 115664). 489 (0.1522) nodes with in-deg > avg deg (72.0), 88 (0.0274) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.example.png.png'
plot 	"inDeg.example.png.tab" using 1:2 title "" with linespoints pt 6
