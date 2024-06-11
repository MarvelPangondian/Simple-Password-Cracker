#!/bin/bash

success=false

python test/test.py
if [ $? -eq 0 ]; then
    success=true
fi

if [ "$success" = false ]; then
    py test/test.py
    if [ $? -eq 0 ]; then
        success=true
    fi
fi

if [ "$success" = false ]; then
    python3 test/test.py
    if [ $? -eq 0 ]; then
        success=true
    fi
fi

if [ "$success" = false ]; then
    echo "All attempts to run test.py failed."
fi

read -p "Press any key to continue..."
