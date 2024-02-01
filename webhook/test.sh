#!/bin/bash
#
# test.sh
#
# Uses curl to POST to webhook server 
#

URL_LOCAL="https://0.0.0.0:8090/"
URL_REMOTE="https://7a92-76-91-56-59.ngrok-free.app/"

URL=$URL_LOCAL
#URL=$URL_REMOTE

HEADER="Content-Type: application/json"
DATA="{\"webserviceUrl\":\"$URL\"}" 

echo "URL: $URL"
echo "HEADER: $HEADER"
echo "DATA: $DATA"

curl -X "POST" -H "$HEADER" -d "$DATA" $URL/hello_world --insecure

# reference
#curl -X "POST" -H "Content-Type: application/json" -d '{"webserviceUrl":"https://0.0.0.0:8090/"}' https://0.0.0.0:8090/hello_world --insecure

