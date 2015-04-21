#include <stdio.h>
#include <stdlib.h>


int main()
{
  int i = 3, j=0;

  j  = (++i) * (++i) * (++i);
  printf("  %d   ", j);

  return 0;

}
