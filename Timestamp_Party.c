#include <stdio.h>
#include <time.h>
#include <unistd.h>

#define     AWAITED_ONE   1500000000
#define     RING          printf("%c",7) ;
#define     TIMESTAMP     (unsigned)time(NULL)

int main (int argc, char** argv)
{
    int ctsp ;

    for (;;) {
        ctsp = TIMESTAMP ;
        if (ctsp == AWAITED_ONE)
        {
            break ;
        }
        sleep(0.3) ;
    }

    RING ;
    printf(
        "\n%s\n",
        "************************\n"
        "     Merry Timestamp !  \n"
        "        1500000000      \n"
        "************************"
    ) ;
    RING ;
}
