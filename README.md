# Relayr-test-task

## Preconditions

Python 2.7, please. You will also need Chrome installed and .chromedriver file added to $PATH environment variable as I use Chrome in tests. If occasionally you have Windows installed, unfortunately I have no idea how to run my tests there :)

## Install dependencies

Clone the repo. Then create and activate virtualenv and install dependencies:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Run tests

Run tests:
```
pytest tests.py
```

If you want to run tests in parallel mode (e.g. in 2 threads):
```
pytest -n 2 tests.py
```

Tests have incorrect credentials (of course they do, it's a public repo). If you are really up to running them, please change login and password variables to valid ones in tests.py::TestTest::test_login_positive.