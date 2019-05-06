#!/bin/bash

declare -a arr=("registration" "login" "logout" "view")

while true; do
	echo "xadd mystream \"*\" event_type ${arr[$(($RANDOM % 4))]} user chris" | redis-cli
	sleep 0.1
done
