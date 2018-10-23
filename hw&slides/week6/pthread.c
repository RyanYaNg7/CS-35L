#include <pthread.h>
#include <stdio.h>

int sum = 0;
void *runner (void * param);

int main(int argc, char *argv[])
{
  pthread_t tid, tid2;
  pthread_attr_t attr;

  pthread_attr_init(&attr);
  pthread_create(&tid, &attr, runner, argv[1]);
  // pthread_create(&tid2, &attr, runner, argv[2]);
  pthread_join(tid, NULL);
  // pthread_join(tid2, NULL);
  printf("sum = %d\n", sum);
  return 0;
}

void *runner(void *param)
{
  int i;
  int upper = atoi(param);
  for (i = 1; i <= upper; i++) {
    sum += i;
  }
  pthread_exit(0);
}