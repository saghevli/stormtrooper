#!/bin/bash
#Usage: sh site_get_multiple.sh <iterations> <site1> <site2> <site3> ...etc
# each site should be followed by a y/n for Telex or No Telex
# example: sh site_get_multiple.sh 100 google.com y baidu.com n something.org y yahoo.com n (etc)

argz=("$@")
maxargz="$#"

iter=argz[0]

i=1
while (( i < maxargz ))
do
    site=${argz[$i]}
    ((i += 1))
    telex=${argz[$i]}
    ((i += 1))
    
    for ((j=0; j<iter; j++))
    do
        if [ "$telex" = "y" ]
        then
            echo "Telex $site"
            phantomjs --disk-cache=false --proxy=127.0.0.1:8888 phantom_get.js "$site"
        else
            echo "Nontelex $site"
            phantomjs --disk-cache=false phantom_get.js "$site"
        fi
    done
done

