#!/bin/bash

success=false

python src/main.py
if [ $? -eq 0 ]; then
    success=true
fi

if [ "$success" = false ]; then
    py src/main.py
    if [ $? -eq 0 ]; then
        success=true
    fi
fi

if [ "$success" = false ]; then
    python3 src/main.py
    if [ $? -eq 0 ]; then
        success=true
    fi
fi

if [ "$success" = false ]; then
    echo "All attempts to run main.py failed."
fi
