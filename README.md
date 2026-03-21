# Docker Experience

This is my personal experience of Docker, documented via a GitHub repository.

## Volume Mapping

To implement volume mapping by reflecting a directory on the host machine inside the Docker container, use the `-v` flag:

```bash
docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11-slim
```

Breakdown of the volume mapping `-v $(pwd)/test:/app/test`:

- `$(pwd)/test`: Represents the directory path on the host machine.
- `:`: Used to separate the host path from the container path.
- `/app/test`: The destination path inside the Docker container where the files are mapped.

## Managing Containers

### View Stopped Instances

To see past instances which are stopped but yet to be deleted, use:

```bash
docker ps -a
```

*Note: This means the container's state is saved, even though it is currently stopped.*

### Delete Stopped Instances

In order to delete stopped containers, run:

```bash
docker rm $(docker ps -aq)
```

*(The `-q` flag is added to only return the container IDs, which `docker rm` requires).*

### Auto-Remove on Exit

It is best practice to add the `--rm` flag in advance so the container cleans up after itself and is deleted automatically when you exit:

```bash
docker run -it --rm ubuntu
```