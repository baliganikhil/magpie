#!/bin/bash

target_folder=$1
tmp_folder=../../../tmp

if [ -z "$target_folder" ]; then
    echo Target folder has not been passed
    exit 1
fi;

cd $target_folder
mkdir node_modules

echo Installing AWS Serverless Express...
# npm install aws-serverless-express --save

echo cd $tmp_folder


# git clone https://github.com/awslabs/aws-serverless-express.git && cd aws-serverless-express/examples/basic-starter