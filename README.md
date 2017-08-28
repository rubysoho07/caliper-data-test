# Caliper Data Test

Tester program for putting data to OpenLRW.

## Prerequisites

* Python 2.x or 3.x
* OpenLRW ([GitHub](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW))
* MongoDB

## How to Build the Environment for Development

1. Install OpenLRW

See `README.md` file in OpenLRW GitHub.
2. Build virtual environment with `virtualenv`
```
$ pip install virtualenv
$ virtualenv caliper-test-env
$ cd caliper-test-env
$ source ./activate
```

3. Install packages with `pip`
```
$ pip install -r requirements.txt
```

## How to Use This Example

### Input Sample Data

* Check your API key for OpenLRW from MongoDB. ([Link](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW#how-to-find-your-openlrw-api-key-and-secret))
* Copy `apiKey` value.
* Paste copied `apiKey` into "Authorization" header of `data_input.py`.
```python
headers = {
    "Authorization": "Your API Key",
    "Content-Type": "application/json"
}
```
* Check the path of sample data file of `data_input.py`.
```python
with open("Path of Your Sample Data") as f:
    for line in f:
        pass
```
* Run script
```
$ python data_input.py
```

