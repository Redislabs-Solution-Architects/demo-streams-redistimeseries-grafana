docker run -p 6379:6379 -it --rm redislabs/redistimeseries
docker run  --rm   -p 3000:3000   --name=grafana   -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource"   grafana/grafana

