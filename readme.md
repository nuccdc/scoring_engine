# Scoring Engine

This project models the scoring engine used in the
[CCDC](http://www.nationalccdc.org/), with some notable improvements to both
the front end UI and scalability.

## Scalable Design

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
