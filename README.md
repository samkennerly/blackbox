# blackbox

Write Python code in any format you like, as long as it's [Black].

<img
  alt="monolith"
  src="https://raw.githubusercontent.com/samkennerly/posters/master/blackbox.jpeg"
  title="Also sprach Zarathustra.">

[Black]: https://github.com/psf/black


## abstract

**Blackbox** is a [shell script] which runs [Black] in a [Docker container].

Black is a program which forces Python code to comply with common style guidelines.

I like Black, but I don't want to install it in all of my Python projects, so I run it in a container.

[shell script]: https://en.wikipedia.org/wiki/Shell_script
[Docker container]: https://docs.docker.com/get-started/


## basics

The `blackbox` script does several things:

- Download an official Python [base image].
- Build a [Docker image] named `blackbox:latest`.
- Run a [self-destructing] container from that image.
- [Mount] the [current folder] into the container.
- Run `black` in the container.

The first time this script is run, Docker may need a few minutes to build an image.

[base image]: https://hub.docker.com/_/python
[Docker image]: https://docs.docker.com/get-started/
[self-destructing]: https://docs.docker.com/engine/reference/run/#clean-up---rm
[Mount]: https://docs.docker.com/storage/bind-mounts/
[current folder]: https://en.wikipedia.org/wiki/Working_directory


## commands

Run `blackbox [PATH]` to reformat and **overwrite** the file `test/clean.py`:
```bash
blackbox test/clean.py
```

Any extra [arguments] are passed to Black. To see all options, read the [docs] or run:
```bash
blackbox --help
```

Dockerbash should delete its own container. If that doesn't work, this will delete it:
```bash
docker rm --force blackbox
```

To see all Docker containers on your machine:
```bash
docker ps --all
```

See the [dockerbash] repo for my personal favorite Docker commands.

[arguments]: https://en.wikipedia.org/wiki/Command-line_interface#Arguments
[docs]: https://black.readthedocs.io/en/stable/installation_and_usage.html#command-line-options
[leftovers]: https://docs.docker.com/engine/reference/commandline/system_prune/
[dockerbash]: https://github.com/samkennerly/dockerbash


## dependencies

1. Docker for [Linux], [Mac], or [Windows].

[Linux]: https://docs.docker.com/install/
[Mac]: https://docs.docker.com/v17.12/docker-for-mac/install/
[Windows]: https://docs.docker.com/docker-for-windows/install/


### installation

1. Copy the [blackbox] script to any folder on machine.
2. Add the script to your system [PATH] if you want to.
3. Ensure the `blackbox` script is [executable].

[blackbox]: blackbox
[executable]: https://en.wikipedia.org/wiki/Chmod
[PATH]: https://en.wikipedia.org/wiki/PATH_%28variable%29


### uninstallation

1. Delete the `blackbox` script.
2. Delete the `blackbox` Docker image: `docker rmi blackbox`


## examples

Format and **overwrite** every relevant file in the current folder:
```bash
blackbox .
```

Format and **overwrite** all `.py` files in `example/folder`:
```bash
blackbox example/folder/*.py
```

Inspect `example/script.py`, but do not modify any files:
```bash
blackbox --check example/script.py
```


## faq

### Where are the configuration files?

Blackbox comes in any color you like as long as it's [black].

[black]: https://black.readthedocs.io/en/stable/the_black_code_style.html

### Why rebuild the image on every run?

Rebuilding wastes a few seconds of computing time, but it saves [brain].

[brain]: https://en.wikipedia.org/wiki/Don%27t_Make_Me_Think
