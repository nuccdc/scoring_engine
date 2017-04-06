# postgres container adapted from https://docs.docker.com/engine/examples/postgresql_service/#installing-postgresql-on-docker
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

# change the password of the postgres user
run echo "postgres:postgres" | chpasswd

user postgres

# postgres initial setup
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE DATABASE scoring_engine;" &&\
    psql --command "CREATE USER scoring_engine WITH PASSWORD 'scoring_engine';" &&\
    psql --command "ALTER ROLE scoring_engine SET client_encoding TO 'utf8';" &&\
    psql --command "ALTER ROLE scoring_engine SET default_transaction_isolation TO 'read committed';" &&\
    psql --command "ALTER ROLE scoring_engine SET timezone TO 'UTC';" &&\
    psql --command "GRANT ALL PRIVILEGES ON DATABASE scoring_engine TO scoring_engine;"
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

# expose database port
EXPOSE 5432

# the startup command
CMD ["/usr/lib/postgresql/9.5/bin/postgres", "-D", "/var/lib/postgresql/9.5/main", "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf"]
