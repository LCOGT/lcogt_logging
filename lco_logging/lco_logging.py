import logging
import json


class LCOFormatter(logging.Formatter):
    """
    A custom log formatter that defauls to LCO's logging conventions.

    Additionally handles calls to logging that pass in a dictionary
    with a top level of "tags" to the extra argument.
    """

    FMT = '%(asctime)s.%(msecs).03d %(levelname)s: %(module)s: %(message)s'
    DATEFMT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, fmt=FMT, datefmt=DATEFMT):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        if 'tags' in record.__dict__:
            record.msg = '{0} | {1}'.format(
                record.msg,
                json.dumps(record.__dict__['tags'])
            )
        return logging.Formatter.format(self, record)
