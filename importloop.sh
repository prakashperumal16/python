#!/bin/bash

i=0
for filename in /Users/prakash/work/21done/Repo/python/images/json/*.json; do
    [ -e "$filename" ] || continue
    echo " Files are " $filename
    mongoimport --uri="mongodb+srv://root:CGgbduBYdEHppjFS@cluster0.bcjgv.mongodb.net/21done-dev?authSource=admin" --db=21done-dev --collection createserviceproviders --file $filename --jsonArray
    # mongoimport --uri="mongodb+srv://root:rootjourney@cluster-21done-prd.xkbvr.mongodb.net/21done-prod-v2?authSource=admin" --db=21done-prod-v2 --collection createserviceproviders --file $filename --jsonArray
    ((i=i+1))
done

echo "uploaded " $i "Files"

