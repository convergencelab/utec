# Untitled Evolutionary Computation 

# Setup

## Windows

Have administrative privileges and run from cmd

```sh
python -m venv --clear --prompt utec venv
venv\Scripts\activate.bat
pip install --upgrade pip setuptools wheel
pip install --editable .
```

## Bash

```sh
python3.10 -m venv --clear --prompt utec venv
. venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --editable .
```


# Formatter

```sh
format # just type this
```


# Unit Tests

```sh
python -m unittest # May need python3
```
