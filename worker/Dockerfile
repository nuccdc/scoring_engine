from ubuntu:16.04

run mkdir /opt/scoring_engine/
workdir /opt/scoring_engine/

# copy build files
copy apt-requirements.txt .
# remove me in production
copy apt-development-requirements.txt .
copy pip-requirements.txt .

# install apt dependencies
run apt -y update
run cat apt-requirements.txt | xargs apt -y install
# remove me in production
run cat apt-development-requirements.txt | xargs apt -y install

# install pip dependencies
run pip install --upgrade pip
run pip install -r pip-requirements.txt

cmd ./test
