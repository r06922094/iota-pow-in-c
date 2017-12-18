reset
set ylabel 'time(sec)'
set xlabel 'loop count'
set style fill solid
set title 'perfomance comparison'
set term png enhanced font 'Verdana,10'
set output 'loop_runtime.png'

plot [:][:]'output.txt' using 2:xtic(1) with histogram title 'OpenCL', \
'' using ($0+0.01):($2+0.001):2 with labels title ' ', \
