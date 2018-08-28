#!/bin/bash

target_folder=$1
aws_serverless_package_name=$2

if [ -z "$target_folder" ]; then
    echo Target folder has not been passed
    exit 1
fi;

if [ -z "$aws_serverless_package_name" ]; then
    echo AWS Serverless package name has not been passed
    exit 1
fi;

cd $target_folder
mkdir node_modules

echo Installing AWS Serverless Express...
# npm install aws-serverless-express --save

# git clone https://github.com/awslabs/aws-serverless-express.git
# rm -rf aws-serverless-express
# mv aws-serverless-express/examples/basic-starter/* .
# npm install

npm install --save-dev nodemon