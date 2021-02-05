# prototypes
Generic utilities I reuse in multiple projects

# aio-test

Minimal aiohttp test server to quickly test that the installed version of aiohttp works.

# docker-git

Docker container that manages its own data volume as a git repo. Contains a python utility that dynamically combines multiple branches using group consensus.

Mount the key, the wrapper script will also set the config parameters from env variables for credentials at runtime.

```
docker run -it -v <ssh key location>:/home/user/.ssh -e gitemail="<git email>" -e gitusername="git username" dockerssh
```

# jupyterlab-custom

Example of how to create a custom Jupyterlab image which replicates your current Python development environment.

```
docker run --rm -p 8888:8888 -v "$PWD":/home/jovyan/work --network=host jupytercustom
```
