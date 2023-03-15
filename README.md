# Template

template is a Python script to create boilerplate projects.

(**See also:** `template`'s older brother, [`boyl`][boyl]!)

[boyl]: https://github.com/mikeevmm/boyl

## Installation

To install this script, clone the repository and run the install script.

```bash
git clone --recurse-submodules https://github.com/mikeevmm/template
cd template
bash install.sh
```

If you'd rather not use the included templates, you can omit
`--recurse-submodules` and configure your `TEMPLATES_DIR` accordingly.

## Usage

```shell
template new --template default . new_project
```

will create a default boilerplate project at `./new_project`.

See

```shell
template --help
```

for further information on command line usage.

New templates should be added to the templates folder, specified by
the `TEMPLATES_DIR` environment variable, by default in the installation
directory of this utility.

Each template is contained in a folder with the template's title, and
is just a boilerplate project to be copied to the target location using
the command line utility.

## Contributing

Contributions are welcome, though you should not expect the project
to be closely maintained. However, the library is robust and, in principle,
final.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
