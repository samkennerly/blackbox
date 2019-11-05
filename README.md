# blackbox

## abstract

[Black](https://github.com/psf/black)
automatically formats Python code.

**Blackbox** is a
[shell script](https://en.wikipedia.org/wiki/Shell_script)
which runs Black in a
[Docker container](https://docs.docker.com/get-started/).

Disclaimer:
Blackbox is not an official project of the
[Python Software Foundation](https://github.com/psf).

## basics

Blackbox does several things:

- Download an official Python
[base image](https://hub.docker.com/_/python).
- Build a
[Docker image](https://docs.docker.com/get-started/)
named `blackbox:latest` with `black` installed.
- Run a
[self-destructing](https://docs.docker.com/engine/reference/run/#clean-up---rm)
container from the `blackbox:latest` image.
- [Mount](https://docs.docker.com/storage/bind-mounts/)
the current
[working directory](https://en.wikipedia.org/wiki/Working_directory)
so the container can access it.
- Run `black` and pass any extra
[arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
to it.

The `blackbox` script rebuilds the `blackbox:latest` image every time it is run.
On the first run, Docker may spend a few minutes downloading things.
Subsequent runs should only take a few seconds.

## commands

`blackbox` is the only command.
See Black's
[docs](https://black.readthedocs.io/en/stable/installation_and_usage.html#command-line-options)
or run `blackbox --help` for options.

Blackbox creates a Docker image on your machine.
To see all Docker images:
```bash
docker image ls
```

Blackbox should clean up after itself.
If it does not, then remove any
[Docker leftovers](https://docs.docker.com/engine/reference/commandline/system_prune/)
by running:
```bash
docker system prune
```

See
[dockerbash](https://github.com/samkennerly/dockerbash)
for other common Docker commands.

## dependencies

1. Docker for
[Linux](https://docs.docker.com/install/),
[Mac](https://docs.docker.com/v17.12/docker-for-mac/install/),
or
[Windows](https://docs.docker.com/docker-for-windows/install/).

### installation
1. Copy the
[blackbox](blackbox)
script.
2. Ensure the script is
[executable](https://en.wikipedia.org/wiki/Chmod).
3. Consider adding the script to your system
[PATH](https://en.wikipedia.org/wiki/PATH_%28variable%29).

### uninstallation
1. Delete the `blackbox` script: `rm path/to/blackbox`
2. Delete the `blackbox` image: `docker rmi blackbox`
3. Delete any Docker leftovers: `docker system prune`

## examples

Inspect `example/script.py`, but do not modify any files:
```bash
blackbox --check example/script.py
```

Format and **overwrite** `example/script.py`:
```bash
blackbox example/script.py
```

Format and **overwrite** all `.py` files in `example/folder`:
```bash
blackbox example/folder/*.py
```

## faq

### Where are the configuration files?

Blackbox comes in any color you like as long as it's
[black](https://black.readthedocs.io/en/stable/the_black_code_style.html).

### Why rebuild the image on every run?

Rebuilding wastes computer time but conserves
[cognitive effort](https://en.wikipedia.org/wiki/Don%27t_Make_Me_Think).

