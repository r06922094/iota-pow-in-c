reset
set ylabel 'time(sec)'
set xlabel '# of threads'
set style fill solid
set title 'perfomance comparison'
set term png enhanced font 'Verdana,10'
set output 'thread_runtime.png'

plot [:][:]'output.txt' using 2:xtic(1) with histogram title 'Pure C', \
'' using ($0-0.08):($2+0.005):2 with labels title ' ', \
'' using 3:xtic(1) with histogram title 'SSE'  , \
'' using ($0+0.1):($3+0.002):3 with labels title ' ', \
