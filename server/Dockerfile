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

# add unprivileged scoring_engine
run useradd -ms /bin/bash scoring_engine
run echo "scoring_engine:scoring_engine" | chpasswd

# add unprivileged worker user
run useradd -ms /bin/bash worker
run echo "worker:worker" | chpasswd

cmd python manage.py migrate && python manage.py runserver 0.0.0.0:8000
