# epochis

A CLI to convert offsets from epoch to human readable dates

# Usage
```bash
$ epochis --help
Usage
	epochis {date}{unit}
Example
	epochis 604m
Supported Units
	m:  months since epoch
	d:  days since epoch
	s:  seconds since epoch
	ms: milliseconds since epoch
```

## Examples

```bash
# months since epoch
$ epochis 604m
2020-05

# days since epoch
$ epochis 18409d
2020-05-26

# seconds since epoch
$ epochis 1590537600s
2020-05-26 00:00:00

# milliseconds since epoch
$ epochis 1590537600ms
2020-05-26 00:00:00.000
```

# Timezone support
All dates are in UTC. Timezone support may be added in the future.

# Why doesn't this use third-party libraries?
There are plenty of libraries to choose from for functionality such as CLI args parsing so why didn't I use them?
This project is just for fun so why not? I like to practice by writing functionality from scratch.

# Dev Notes
To install locally as standalone CLI
```
python setup.py install
```

To upload to pypi
```
python setup.py sdist
twine upload dist/*
```

To run unit tests
```
python -m unittest
```
