from ubuntu:16.04

run mkdir /opt/scoring_engine/
workdir /opt/scoring_engine/

# copy build files
copy apt-requirements.txt .
# remove me in production
copy apt-development-requirements.txt .

# install apt dependencies
run apt -y update
run cat apt-requirements.txt | xargs apt -y install
# remove me in production
run cat apt-development-requirements.txt | xargs apt -y install

# set up the scoring_engine user
run useradd -ms /bin/bash scoring_engine
run echo "scoring_engine:scoring_engine" | chpasswd

# configure rabbitmq
copy rabbitmq.config /etc/rabbitmq/

cmd rabbitmq-server
