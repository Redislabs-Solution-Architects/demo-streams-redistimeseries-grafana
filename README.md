# Redis Time Series + Streams + Grafana

1) run the following docker containers

```
docker run -p 6379:6379 -it --rm redislabs/redistimeseries
docker run  --rm   -p 3000:3000   --name=grafana   -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource"   grafana/grafana
```

2) Start up the random generator

```
./add_events.sh
```

3) Setup and run the importer

```
pip install -r requirements.txt
./example.py
```

4) Run Data source

```
python GrafanaDatastoreServer.py
```

5) Navigate to 

http://localhost:3000

Add a SimpleJSON data source
http://<IPADDRESSOFLAPTOP>:8080/

6) Create a dashboard
