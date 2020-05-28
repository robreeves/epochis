# epochis

A CLI to convert offsets from epoch to dates

# Usage
`epochis 604m` --> `2020-05 UTC`<br />
`epochis 18409d` --> `2020-05-26 UTC`<br />
`epochis 1590537600s` --> `2020-05-26 00:00:00 UTC`<br />
`epochis 1590537600ms` --> `2020-05-26 00:00:00.000 UTC`<br />

## Timezone support (TODO)
`epochis 604m PST` --> `2020-05 PST`

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
