#!/usr/bin/env bash

target_folder=$1
mongoose_package_names=$2

if [ -z "$target_folder" ]; then
    echo Target folder has not been passed
    exit 1
fi;

if [ -z "$mongoose_package_names" ]; then
    echo AWS Serverless package name has not been passed
    exit 1
fi;

cd $target_folder
mkdir node_modules

echo Installing Mongoose libraries...
npm install $mongoose_package_names --save