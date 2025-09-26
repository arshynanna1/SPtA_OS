#!/bin/bash


cd /etc || exit 1


file_count=$(find . -maxdepth 1 -type f | wc -l)


echo "count files: $file_count"
