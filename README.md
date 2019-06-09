# Redis Time Series + Streams + Grafana

1) run the docker containers from Docker compose

```
sudo chown -R 472:472 grafana-data/
docker-compose up
```

2) Start up the random generator

```
./add_events.sh
```

3) Navigate to 

http://localhost:3000

User: admin
Password: 1234

Click on dashboards and Example Dash

