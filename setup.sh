#!/bin/bash

git submodule init
git submodule update

pushd generalised-brown/merge_generator
make 
popd
