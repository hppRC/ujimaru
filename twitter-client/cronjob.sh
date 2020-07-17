#!/bin/bash
cd ~/ghq/github.com/hppRC/ujimaru/twitter-client

# source Twitter API tokens and keys
source .envrc

./target/release/twitter-client
