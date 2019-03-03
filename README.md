# Example Python packaging using Azure Devops Matrix

## Goals
Demonstrate the use of `matrix` in Azure Pipelines yaml builds for generation of a Python package using different versions of Python.

### Final state
- published containers for each Python version
- docker tags showing both python version and the Package version
- latest tag for a specific default version of Python and current Package
- shows up in a registry, `localhost:5000` in the walk-through, using registry API v2:

#### Calling registry API v2
```
curl -i http://localhost:5000/v2/az-matrix/tags/list
```

#### Output
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Docker-Distribution-Api-Version: registry/2.0
...

{"name":"az-matrix","tags":["latest"]}

```


> NOTE: these examples use a local docker registry. The details on running, configuration, etc. is found here [Docker: Deploying a registry server](https://docs.docker.com/registry/deploying/)


## Running the local registry

### Docker registry container

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

