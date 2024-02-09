

#host="http://localhost:8080"
path="/invoke/blah"

header='Content-Type: application/json'
data='{"name":"Bob"}'

echo "host: $host"
echo "path: $path"
echo "header: $header"
echo "data: $data"

curl -X "POST" -H "$header" -d "$data" $host$path

#curl -X "POST" -H "Content-Type: application/json" -d '{"name":"Bob"}' http://localhost:8080/invoke/blah
#curl -X "POST" -H "Content-Type: application/json" -d '{"name":"Bob"}' https://bcb0-64-124-71-89.ngrok-free.app/invoke/blah
