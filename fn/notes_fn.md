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
fn start --log-level DEBUG
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


## OCI stuff

Oracle Functions & tags
https://blogs.oracle.com/cloud-infrastructure/post/working-with-oracle-functions-and-tag-defaults

Creating Functions from Existing Docker Images
https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm

(Mac) Install `oci-cli` with Homebrew 
```
brew install oci-cli
```

Oracle CLI Getting Started
https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm#GettingStartedwiththeCommandLineInterface


```
oci os ns get
oci iam compartment list 
oci iam compartment list -c <tenancy_id>
```

Use oci cli fn application create
```
#oci fn application create -c ocid1.compartment.oc1..3nkmscz63iyndbvpdnl7bykk37jqmf43ahymba --display-name helloworld-java-app --subnet-ids '["ocid1.subnet.oc1.ca-montreal-1.dy5hdvgtgrhsxchuvgkbqqxd4rqz4oeuknkkgba"]' --defined-tags '{"OracleInternalReserved": {"CostCenter": "8675309"}}'
oci fn application create -c ocid1.compartment.oc1..3nkmscz63iyndbvpdnl7bykk37jqmf43ahymba --display-name helloworld-java-app --subnet-ids '["ocid1.subnet.oc1.ca-montreal-1.dy5hdvgtgrhsxchuvgkbqqxd4rqz4oeuknkkgba"]' --defined-tags '{"OracleInternalReserved": {"CostCenter": "8675309"}}'
```

Cost_Tagging .  Project_Key : Labs_Ops

what compartment?

error on Functions function page (e.g. hello6):
Compartment: Error fetching data
```
fn build
fn push
```


