//tr2b.c buffered

#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

int checkDuplicate(const char* str, char c);

int main(int argc, const char* argv[]){
  const char* from, * to;
  int i;
  if(argc != 3){
    fprintf(stderr, "Wrong number of operands\n");
    exit(1);
  }
  from = argv[1];
  to = argv[2];
  int len_from = strlen(from);
  int len_to = strlen(to);
  if(len_from == 0){
    fprintf(stderr, "Missing operand\n");
    exit(1);
  }
  if(len_from != len_to){
    fprintf(stderr, "Different Length of input and output\n");
    exit(1);
  }
  
  for(i=0; i<len_from; i++){
    if(checkDuplicate(from, from[i])){
      fprintf(stderr, "Duplicate bytes in FROM string\n");
      exit(1);
    }
  }

  size_t len;
  size_t length_from = strlen(from);
  for(;;){
    char gchar = getchar();

    if(ferror(stdin)){
      fprintf(stderr, "Error input string");
      exit(1);
    }

    if(feof(stdin))
      break;

    int printed = 0;
    for (i=0; i<length_from; i++){
      if(from[i]==gchar){
      putchar(to[i]);
      printed = 1;
      }
    }
    if(printed == 0)
      putchar(gchar);

    if(ferror(stdout)){
      fprintf(stderr, "Error output string");
      exit(1);
    }
  }
  return 0;

}

int checkDuplicate(const char* str, char letter){
 int i = 0;
  for(;*str != '\0'; str++){
    if(*str == letter){
      i++;
      if(i > 1)
      return 1;
    }
  }
  return 0;
}
