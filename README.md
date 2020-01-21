# blackbox

Write Python code in any format you like, as long as it's *Black*.

<img
  alt="monolith"
  src="https://raw.githubusercontent.com/samkennerly/posters/master/blackbox.jpeg"
  title="Also sprach Zarathustra.">

## abstract

**Blackbox** is a [shell script] which runs [Black] in a [Docker container].

Disclaimer: Blackbox is not an official [PSF] project.
It's just a convenience script.

[shell script]: https://en.wikipedia.org/wiki/Shell_script
[Black]: https://github.com/psf/black
[Docker container]: https://docs.docker.com/get-started/
[PSF]: https://github.com/psf

## basics

Blackbox does several things:

- Download an official Python [base image].
- Build a [Docker image] named `blackbox:latest` with `black` installed.
- Run a [self-destructing] container from the `blackbox:latest` image.
- [Mount] the current [working directory] so the container can access it.
- Run `black` and pass any extra [arguments] to it.

The `blackbox` script rebuilds the `blackbox:latest` image every time it is run.
On the first run, Docker may spend a few minutes downloading things.
Subsequent runs should only take a few seconds.

[base image]: https://hub.docker.com/_/python
[Docker image]: https://docs.docker.com/get-started/
[self-destructing]: https://docs.docker.com/engine/reference/run/#clean-up---rm
[Mount]: https://docs.docker.com/storage/bind-mounts/
[working directory]: https://en.wikipedia.org/wiki/Working_directory
[arguments]: https://en.wikipedia.org/wiki/Command-line_interface#Arguments

## commands

`blackbox` is the only command.
See Black's [docs] or run `blackbox --help` for options.

Blackbox creates a Docker image on your machine.
To see all Docker images:
```bash
docker image ls
```

Blackbox should clean up after itself.
If it does not, then remove any [leftovers] by running:
```bash
docker system prune
```

See [github.com/samkennerly/dockerbash] for other common Docker commands.

[docs]: https://black.readthedocs.io/en/stable/installation_and_usage.html#command-line-options
[Docker leftovers]: https://docs.docker.com/engine/reference/commandline/system_prune/
[github.com/samkennerly/dockerbash]: https://github.com/samkennerly/dockerbash

## dependencies

1. Docker for [Linux], [Mac], or [Windows].

[Linux]: https://docs.docker.com/install/
[Mac]: https://docs.docker.com/v17.12/docker-for-mac/install/
[Windows]: https://docs.docker.com/docker-for-windows/install/

### installation

1. Copy the [blackbox] script.
2. Ensure the script is [executable].
3. Consider adding the script to your system [PATH].

[blackbox]: blackbox
[executable]: https://en.wikipedia.org/wiki/Chmod
[PATH]: https://en.wikipedia.org/wiki/PATH_%28variable%29

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

Blackbox comes in any color you like as long as it's [black].

[black]: https://black.readthedocs.io/en/stable/the_black_code_style.html

### Why rebuild the image on every run?

Rebuilding wastes a few seconds of computing time to conserve [brain].

[cognitive effort]: https://en.wikipedia.org/wiki/Don%27t_Make_Me_Think
