#!/bin/bash
# Author : Yoshiyuki Kurose
# This script is bash script on 'Ubuntu 22.04 LTS' version.
# So, In this script, I use `apt` command.

PROJECT_ROOT=$(pwd)


function locationErrorMsg() {
    local LOCATION_ERROR_MSG="Is this dir correct location?"
    echo "$LOCATION_ERROR_MSG";
    return 1
}

git clone https://github.com/yoshiyuki-140/CivicSeek.git
cd CivicSeek || locationErrorMsg
python3 -m pip venv venv # python仮想環境venv起動準備
./venv/bin/activate # 仮想環境起動
cd ./setup
source regenerate_key.sh || locationErrorMsg
cd ..
