#!/bin/bash

for itemName in queued_updates/items/*.json; do
    itemName=$(basename "$itemName")
    if [[ -f "dump/items/$itemName" ]]; then
        echo ""
        echo "====> File: $itemName"
        diff --color "dump/items/$itemName" "queued_updates/items/$itemName"
        read -p "Press enter to continue"
    fi
done