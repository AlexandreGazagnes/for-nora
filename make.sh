#! /bin/sh

# update & upgrade
apt update -y && apt upgrade -y

# install
apt install htop nano python3-pip python3-venv -y

# env
# python3 -m venv env
# source env/bin/activate

# pip
pip install -r requirements.txt

# test
which python >> conf.log
python -c "import pandas;" >> conf.log