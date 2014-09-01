# docker-stop-test

Experiments on the behavior of docker stop and docker kill commands.


## Purpose

This is a collection of dockerfiles and scripts to check the behavior of `docker stop` and
`docker kill` commands in relation to how the contained processes are killed, what is their
exit status, and what is the exit status of the containing docker process.


## Sample runs

Native:

```
$ bin/interruptible/test-native
[bash] starting main process in background
[bash] temporary directory: /tmp/tmp.VHGOJIeyWq
[bash] waiting
[bash] process launched with pid 8075
[bash] killing process
[bash] program output:
[test] started with PID 8075
[test] GOT SIGNAL 15
```

Docker with PID 1:

```
$ bin/interruptible/test-docker-pid-1
[bash] running in docker with PID 1
[bash] temporary directory: /tmp/tmp.Bbjx9D4ewk
[bash] docker container 848e0d7b961215ed4dd9f2bbba6a2a64d566e82454918c17aeb3257d6636d789 launched
[bash] waiting
[bash] stopping docker container
848e0d7b961215ed4dd9f2bbba6a2a64d566e82454918c17aeb3257d6636d789
[bash] container exit code:         "ExitCode": 1,
[bash] program output:
[test] started with PID 1
[test] GOT SIGNAL 15
```

Docker with phusion-baseimage:

```
$ bin/interruptible/test-phusion-baseimage-python
[bash] building docker image
Sending build context to Docker daemon  2.56 kB
Sending build context to Docker daemon
[bash] running in docker with phusion-baseimage
[bash] temporary directory: /tmp/tmp.L5bpdHoquV
[bash] docker container c963d9816f722be99013914660aefccf1a68570ab2a31b6df2d11a939acae432 launched
[bash] waiting
[bash] stopping docker container
c963d9816f722be99013914660aefccf1a68570ab2a31b6df2d11a939acae432
[bash] container exit code:         "ExitCode": 2,
[bash] program output:
[test] started with PID 97
[test] GOT SIGNAL 15
```
