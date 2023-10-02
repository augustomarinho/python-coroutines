<div align="center">
<h1>Python Coroutines</h1>
<div>
    <img src="https://img.shields.io/badge/FastAPI-Python%203.11-blue.svg" alt="FastAPI supports Python 3.11"/>    
    <a href="https://python-poetry.org/"><img src="https://img.shields.io/badge/maintained%20with-poetry-rgb(30%2041%2059).svg" alt="poetry"/></a>
</div>
</div>

<p>This project was created to study the use of coroutines in Python. These concepts are applied in standalone and web apps (using FastAPI), implementing simple CPU-Bound and IO-Bound algorithms to validate the behavior.</p>
<br>


* [Installation](#installation)
    * [Poetry](#poetry)
    * [dependencies](#dependencies)
    * [Running](#running)
        * [Standalone](#standalone)
        * [Web](#web)
    * [Testing](#testing)
    * [Locust](#locust)

 
# Installation 

## Poetry
This project uses [Poetry](https://python-poetry.org/) as a dependency manager. To install it, run the following command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Dependencies
```bash
poetry install
```
## Running
### Standalone
For running standalone examples we can run the following commands:
```bash
cd python-coroutines
export PYTHONPATH=$PYTHONPATH:$(pwd)
poetry shell
python coroutines/corroutine_1.py
```

### Web
For running web examples we can run the following commands:
```bash
cd python-coroutines
poetry run uvicorn main:app --workers 10 --reload
```

## Testing
```bash
curl -X GET http://localhost:8282/6/async-cpu-bound
curl -X GET http://localhost:8282/6_1/async-cpu-bound
curl -X GET http://localhost:8282/6_2/async-cpu-bound
curl -X GET http://localhost:8282/6_3/async-cpu-bound
```

```bash
curl -X GET http://localhost:8282/7/async-io-bound
curl -X GET http://localhost:8282/7_1/async-io-bound
curl -X GET http://localhost:8282/7_2/async-io-bound
curl -X GET http://localhost:8282/7_3/async-io-bound
```

## Locust
```bash
poetry run locust -f locust/locustfile_case7.py -H "http://localhost:8282" -P 8090
poetry run locust -f locust/locustfile_case6.py -H "http://localhost:8282" -P 8090
```

