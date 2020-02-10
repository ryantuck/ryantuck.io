# docker

Run a container interactively:

```
docker run -it <image-name> /bin/bash
```

Or, if the `ENTRYPOINT` is set on the container instead of `COMMAND`, override it like so:

```
docker run -it --entrypoint /bin/bash arrakis
```
