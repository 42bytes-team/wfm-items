#!/bin/bash

for itemName in queued_updates/items/*.json; do
    itemName=$(basename "$itemName")
    if [[ -f "items/$itemName" ]]; then
        echo ""
        echo "====> File: $itemName"
        diff "queued_updates/items/$itemName" "items/$itemName"
        read -p "Press enter to continue"
    fi
done