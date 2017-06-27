#!/bin/sh

awaited=1500000000
cts=0
to_ts=1

while [ $to_ts -gt 0 ]
do
    cts=$(date +%s)
    to_ts=$(($awaited-$cts))

    sleep 0.3
done


echo -e "\a"

echo -e "\n
    ************************\n
         Merry Timestamp !  \n
            1500000000      \n
    ************************\n"

echo -e "\a"
