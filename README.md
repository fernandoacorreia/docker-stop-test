# docker-stop-test

Experiments on the behavior of docker stop and docker kill commands.


## Purpose

This is a collection of dockerfiles and scripts to check the behavior of `docker stop` and
`docker kill` commands in relation to how the contained processes are killed, what is their
exit status, and what is the exit status of the containing docker process.


## Sample runs

Native:

```
$ bin/test-native
[bash] starting main process in background
[bash] temporary directory: /tmp/tmp.3q474f8Xhy
[bash] waiting
[bash] process launched with pid 6359
[bash] killing process
[bash] program output:
[test] started with PID 6359
[test] GOT SIGNAL 15
```

Docker with PID 1:

```
$ bin/test-docker-pid-1
[bash] running in docker with PID 1
[bash] temporary directory: /tmp/tmp.w8WM8kvXPf
[bash] docker container 92b1f43a03c9ae0fc68c8ec5b0ff9eb403201e21b1d8b4ac434a15363970b24d launched
[bash] waiting
[bash] stopping docker container
92b1f43a03c9ae0fc68c8ec5b0ff9eb403201e21b1d8b4ac434a15363970b24d
[bash] container exit code:         "ExitCode": 1,
[bash] program output:
[test] started with PID 1
[test] GOT SIGNAL 15
```

Docker with phusion-baseimage:

```
$ bin/test-phusion-baseimage-python
[bash] building docker image
Sending build context to Docker daemon  2.56 kB
Sending build context to Docker daemon
[bash] running in docker with phusion-baseimage
[bash] temporary directory: /tmp/tmp.fF8bPOHUf2
[bash] docker container 64b03d4b21349139c56bbd07b875f18875d917294971ab4c6b120786bedb8ac2 launched
[bash] waiting
[bash] stopping docker container
64b03d4b21349139c56bbd07b875f18875d917294971ab4c6b120786bedb8ac2
[bash] container exit code:         "ExitCode": 2,
[bash] program output:
[test] started with PID 100
[test] GOT SIGNAL 15
```
