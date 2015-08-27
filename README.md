lcogt-logging
=============

`lcogt-logging` defines a single class `LCOGTFormatter` which contains the LCOGT
standard log format definition. Application logs that use this formatter will
adhere to the LCOGT logging standards.

Installation
------------
This module is available on the internal PyPI:
`$ pip install lcogt-logging`

Usage
-----
Set your StreamHandler's formatter to an insatiated LCOGTFormatter:
`stream_handler.setFormatter(LCOGTFormatter())`

More advanced usage, including the use of tags, can be found in example.py:

```
$ python example.py
2015-08-27 11:22:10.588    ERROR:         example: Starting the example | {"pid": 14361, "example": true}
2015-08-27 11:22:10.588 CRITICAL:         example: Log with additional tags | {"foo": "bar", "pid": 14361, "example": true}
2015-08-27 11:22:10.589  WARNING:         example: Log with no tags at all
```

Testing
-------

Install the requirements from `requirements-text.txt`:

`$ pip install -r requirements-test.txt`

Run the tests:

`$ py.test test.py`
