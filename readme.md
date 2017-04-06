# Scoring Engine

This project models the scoring engine used in the
[CCDC](http://www.nationalccdc.org/), with some notable improvements to both
the front end UI and scalability. It is currently under development and not
anywhere near a production-ready state and we're actively interested in
contributors.

## Scalable Design

![design](/docs/design.png?raw=True)

This scoring engine is built around a [Celery](http://www.celeryproject.org/)
distributed task queue which allows us to scale scoring workers to whatever
hardware is available. Individual workers are run as
[docker](https://www.docker.com/) containers which fetch tasks from a
[RabbitMQ](https://www.rabbitmq.com/) server. Scoring results and team
configuration are stored in a [PostgreSQL](https://www.postgresql.org/)
database and accessed via a [Django](https://www.djangoproject.com/) front end.
All servers are run as docker containers and managed by [Docker
Compose](https://docs.docker.com/compose/).

## Plugins

### Included Plugins

- DNS
- FTP
- HTTP
- IMAP
- POP3
- SMTP
- SMB
- MYSQL
- MSSQL
- Ping
- SSH

### Enabled Plugins

Plugins still need to be ported from our [old scoring
engine](https://github.com/ainterr/scoring_engine). Currently enabled plugins
include:

- PING
- DNS

### Adding Plugins

### Dependencies

Docker and docker-compose are the only requirements to get up and running, the
containers will install project dependencies on their own. On ubuntu 16.04:

```bash
sudo apt install docker.io docker-compose
```

## Running

Simply build the containers and run them in daemon mode:

```bash
docker-compose build
docker-compose up -d
```

Then navigate to the web UI at http://localhost:8000/.

### Scaling Workers

A default build will run with a single worker. To increase the number of
workers, simply `docker-compose scale` the worker container.

```bash
docker-compose scale worker=20
```

## License

This project is open source under the MIT public license. See [license.txt](license.txt).
