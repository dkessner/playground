# fn project

## Installation

[Installation tutorial](https://fnproject.io/tutorials/install/)

Install fn:
```console
brew update && brew install fn
```

Start Fn server:
```console
fn start
```

Check that Fn server is running:
```console
fn version
```

List available contexts:
```console
fn list contexts
```

Select context:
```console
fn use context default
```

Local development: set registry to arbitrary value
(registry value -> Docker username for local images)
```console
fn update context registry foobar
```

Normal development: set registry to Docker Hub username
```console
fn update context registry your-docker-hub-user-name
```

## Python intro

[Python tutorial](https://fnproject.io/tutorials/python/intro/)

Create new Fn project in `myfunc` directory, using Python runtime.
```console
fn init --runtime python myfunc
```

Create application
```console
fn create app myapp
```

Deploy function to app (calls `docker build`)
```console
fn --verbose deploy --app myapp --local
```

List stuff
```console
fn list apps
fn list functions myapp
docker images | grep foobar
```

List stuff
```console
fn list apps
fn list functions myapp
docker images | grep foobar
```

Invoke the function
```console
fn invoke myapp myfunc
```

Invoke the function, passing data
```console
echo -n '{"name":"Bob"}' | fn invoke myapp myfunc --
```

Inspect the function (e.g. URL for endpoint)
```console
fn inspect function myapp myfunc
```

Invoke with `curl`
```console
curl -X "POST" -H "Content-Type: application/json" http://url_name
```

Invoke with `curl`
```console
curl -X "POST" -H "Content-Type: application/json" -d '{"name":"Bob"}' http://url_name
```




