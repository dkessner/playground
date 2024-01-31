# notes LIMS webhook

[sapio-py tutorials](https://github.com/sapiosciences/sapio-py-tutorials)
[webhook server example](https://github.com/sapiosciences/sapio-py-tutorials/blob/master/7_webhook_server.py)

Installation
```console
pip install sapiopylib
```

Additional dependencies
```console
pip install waitress
```


Test with curl
```console
curl -X "POST" -H "Content-Type: application/json" -d '{"webserviceUrl":"http://0.0.0.0:8090/"}' http://0.0.0.0:8090/hello_world
```


