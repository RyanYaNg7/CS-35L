Conclusions about how well your implementation of SRT improves its performance:
rm -f *.o *.tmp 1-test.ppm 2-test.ppm 4-test.ppm 8-test.ppm srt srt.tgz
gcc -std=gnu11 -g -O2 -Wall -Wextra -Wno-unused-parameter   -c -o main.o main.c
gcc -std=gnu11 -g -O2 -Wall -Wextra -Wno-unused-parameter   -c -o raymath.o raymath.c
gcc -std=gnu11 -g -O2 -Wall -Wextra -Wno-unused-parameter   -c -o shaders.o shaders.c
gcc -std=gnu11 -g -O2 -Wall -Wextra -Wno-unused-parameter -o srt main.o raymath.o shaders.o -lm -lpthread
time ./srt 1-test.ppm >1-test.ppm.tmp

real 0m49.226s
user 0m48.578s
sys  0m0.001s
mv 1-test.ppm.tmp 1-test.ppm
time ./srt 2-test.ppm >2-test.ppm.tmp

real 0m24.925s
user 0m49.659s
sys  0m0.001s
mv 2-test.ppm.tmp 2-test.ppm
time ./srt 4-test.ppm >4-test.ppm.tmp

real 0m12.010s
user 0m47.323s
sys  0m0.011s
mv 4-test.ppm.tmp 4-test.ppm
time ./srt 8-test.ppm >8-test.ppm.tmp

real 0m8.401s
user 1m4.234s
sys  0m0.007s
mv 8-test.ppm.tmp 8-test.ppm
for file in 1-test.ppm 2-test.ppm 4-test.ppm 8-test.ppm; do \
  diff -u baseline.ppm $file || exit; \
done
	    From the result we get in make-log.txt, we can see that there is a significant improvement of execution time with an inverse relation with the number of threads. By spliting the image into several parts handled by each threads, we realize parellelization.

Problem run into:
1. how to split the image so that they are embarrassingly parallel
2. what to do with the code to make it happen.
