#!/bin/bash

err=0
tot=0

for repo in Howto Examples ; do
    echo "$repo:"
    cd $repo
    for script in *.py ; do
        let tot++
        echo -en "${script} :"
        $(python "${script}" &> /dev/null) && echo " passed." || { echo " failed !"; let err++ ; }
    done
    cd ..
done

echo "total scripts: $tot, failed scripts: $err"
