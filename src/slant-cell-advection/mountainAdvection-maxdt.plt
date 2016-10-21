set term epslatex color size 3.5,2.5

set style data linespoints
set logscale

set xlabel "$\\Delta x$"
set ylabel "$\\Delta t_\\mathrm{max}$" offset 2

unset key

set label at 120,3.2 rotate by 20 "Basic terrain following"
set label at 180,0.6 rotate by 20 "Slanted cells"
set label at 120,0.2 "Cut cells"

plot "`echo $ATMOSTESTS_DIR`/build/mountainAdvection-btf-linearUpwind-collated/0/maxdt.txt" using 1:2 lw 1.5 ps 3, \
     "`echo $ATMOSTESTS_DIR`/build/mountainAdvection-cutCell-linearUpwind-collated/0/maxdt.txt" using 1:2 lw 1.5 ps 3, \
     "`echo $ATMOSTESTS_DIR`/build/mountainAdvection-slantedCell-linearUpwind-collated/0/maxdt.txt" using 1:2 lw 1.5 ps 3