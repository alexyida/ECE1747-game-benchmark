#!/usr/bin/env bash

if [ $# -lt 3 ]
then
  echo "Usage: $0 server_name server_port num_of_clients"
  exit
fi

echo "server_name: $1"
echo "server_port: $2"
echo "num_of_clients: $3"

for (( i = 0; i < $3; i++ )); do
	./client $1:$2 > /dev/null & 
done

echo "started running $i clients"