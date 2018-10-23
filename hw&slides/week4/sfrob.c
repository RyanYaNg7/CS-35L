#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define SPACE   ' '
#define INIT_SIZE   25

char decrypt(const char c);
int  frobcmp(char const* a, char const* b);
int  cmpWrapper(const void* a, const void* b);
void checkMemErr(void* ptr);
void checkIOErr(FILE* p);
void reportErr(const char* msg);
void strWrite(const char* str);
void initLinebuf(char** linebuf, char* buf, size_t size);

int main(void)
{
  int (* cmp) (const void*, const void*);
  char* input, * input2, ** linebuf, curChar;
  size_t lineNum, lineSize, bufferSize, i, fileSize;
  int isEOF, isSpace;
    
  bufferSize = 0, lineNum = 0, lineSize = 0, isEOF = feof(stdin);
  fileSize = INIT_SIZE;
    
  cmp = &cmpWrapper;
    
  input = (char*) malloc(sizeof(char) * fileSize);
  checkMemErr(input);
    

  while (!isEOF)
    {
      curChar = getchar();
      checkIOErr(stdin);
      isSpace = curChar == SPACE;
      isEOF = feof(stdin);
      if (!lineSize && isSpace)
	continue;
      if (bufferSize == fileSize)
        {
	  fileSize *= 2;
	  input2 = (char*) realloc(input, sizeof(char) * fileSize);
	  checkMemErr(input2);
	  input = input2;
        }
        
      if (!isEOF)
        {
	  input[bufferSize++] = curChar;
	  lineSize++;
	  if (!isSpace)
	    continue;
        }
      else
        {
	  if (!bufferSize)
            {
	      free(input);
	      return 0;
            }
	  if (input[bufferSize-1] != SPACE)
	    input[bufferSize++] = SPACE;
	  if (!lineSize)
	    break;
        }
        
      lineNum++;
      lineSize = 0;
    }
  linebuf = (char**) malloc(sizeof(char*) * lineNum);
  checkMemErr(linebuf);
    
  initLinebuf(linebuf, input, bufferSize);
    
  qsort(linebuf, lineNum, sizeof(char*), cmp);
    
  for (i = 0; i < lineNum; i++)
    strWrite(linebuf[i]);
    
  free(linebuf);
  free(input);
  return 0;
}

void reportErr(const char* msg)
{
  fprintf(stderr, "%s an error occured: %d\n", msg, errno);
  exit(1);
}

void checkIOErr(FILE* p)
{
  if (ferror(p))      reportErr("fail to input/output!");
}

void checkMemErr(void* ptr)
{
  if (ptr == NULL)    reportErr("Fail to create memory");
}

char decrypt(const char c)
{
  return c ^ 42;
}

int cmpWrapper(const void* a, const void* b)
{
  return frobcmp(*((const char**) a), *((const char**) b));
}

void strWrite(const char* str)
{
  for (;;)
    {
      putchar(*str);
      checkIOErr(stdout);
      if (*str++ == SPACE)
	return;
    }
}

void initLinebuf(char** linebuf, char* buf, size_t size)
{
  size_t i, lineNum;
  char* line = buf;
  for (i=0, lineNum = 0; i<size; i++)
    {
      if (buf[i] == SPACE)
        {
	  linebuf[lineNum++] = line;
	  line = buf + i + 1;
        }
    }
}

int frobcmp(char const* a, char const* b)
{
  for (; *a == *b; a++, b++)
    if (*a == SPACE)
      return 0;
  return ((decrypt(*a) < (decrypt(*b)) ? -1 : 1));
    
}
