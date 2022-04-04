#!/bin/bash

i = 0
for filename in ~/Desktop/json/*.json; do
    [ -e "$filename" ] || continue
    echo " Files are " $filename
    mongoimport --uri="mongodb+srv://root:rootjourney@cluster-21done-prd.xkbvr.mongodb.net/21done-prod-v2?authSource=admin&replicaSet=atlas-93gpql-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true" --db=21done-prod-v2 --collection createserviceproviders --file $filename --jsonArray
    ((i=i+1))
done

echo "uploaded " $i "Files"