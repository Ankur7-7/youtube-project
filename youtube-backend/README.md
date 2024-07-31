# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Steps to start from scratch ###

* Create a repo on remote
* Clone on locat
* Create virtual env
* Zappa init

### Layer creation ###

```commandline
rm -rf layers/python/*

cp -r venv/lib/python3.9/site-packages/* layers/python/

cd layers

zip -r python.zip python

1. Staging
aws s3 cp python.zip s3://alpha-api-bucket/staging/python.zip --profile benow_kuldeep

aws lambda publish-layer-version --layer-name alpha-apis-staging-layer --description "Alpha APIs requirements.txt libs"  --license-info "MIT" --content S3Bucket=alpha-api-bucket,S3Key=staging/python.zip --compatible-runtimes python3.6 python3.7 python3.8 python3.9 --compatible-architectures "arm64" "x86_64" --profile benow_kuldeep 
2. Production 
aws s3 cp python.zip s3://alpha-api-bucket/production/python.zip --profile benow_kuldeep

aws lambda publish-layer-version --layer-name alpha-apis-production-layer --description "Alpha APIs requirements.txt libs"  --license-info "MIT" --content S3Bucket=alpha-api-bucket,S3Key=production/python.zip --compatible-runtimes python3.6 python3.7 python3.8 python3.9 --compatible-architectures "arm64" "x86_64" --profile benow_kuldeep

```
* Clone on locat
* Create virtual env
* Zappa init
### Who do I talk to? ###

* Repo owner or admin: kuldeep.singh@benow.in
* Other community or team contact: Benow Tech team