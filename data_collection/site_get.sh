#!/bin/sh
#Usage: sh site_get.sh <iterations> <site1> <site2> <telex[y/n]>
#telex site must be second
if [ "$4" = "y" ]
then
    echo "Using telex proxy @ 127.0.0.1:8888"
    for ((i=0; i < $1; i++ ))
    do
        printf '%d of %d\n' $i $1
        phantomjs --disk-cache=false phantom_get.js $2
        phantomjs --disk-cache=false --proxy=127.0.0.1:8888 phantom_get.js $3
        #curl -silent -o curl_out.html $2
        #curl -silent -o curl_out.html $3
    done
else
    echo "standard connection"
    for ((i=0; i < $1; i++ ))
    do
        printf '%d of %d\n' $i $1
        phantomjs --disk-cache=false phantom_get.js $2
        phantomjs --disk-cache=false phantom_get.js $3
        #curl -silent -o curl_out.html $2
        #curl -silent -o curl_out.html $3
    done
fi

