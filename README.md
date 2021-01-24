# TodoList
A primary demo of flask: todolist.

## Installation
clone:

```
$ git clone https://github.com/D-zilch/todolist.git
$ cd todolist
```

create & activate virtual env then install dependency:
with venv/virtualenv + pip:

```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt or pip download -r requirements.txt
```

or with poetry:


```
$ poetry shell
$ poetry install
```


generate fake data then run:

```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
