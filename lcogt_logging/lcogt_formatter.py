#!/usr/bin/env python

'''
Contains code relevant to logging standards

Austin Riba
Aug 2015
'''

import logging
import json


class LCOGTFormatter(logging.Formatter):
    """
    A custom log formatter that defauls to LCOGT's logging conventions.

    The argument "extra_tags" takes a dictionary that will be appended
    to the log message as json.

    Additionally handles calls to logging that pass in a dictionary
    with a top level of "tags" to the extra argument.
    """

    FMT = '%(asctime)s.%(msecs).03d %(levelname)8s: %(module)15s: %(message)s'
    DATEFMT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, fmt=FMT, datefmt=DATEFMT, extra_tags=None):
        self.extra_tags = extra_tags
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        tags = {}
        if 'tags' in record.__dict__:
            tags.update(record.__dict__['tags'])
        if self.extra_tags:
            tags.update(self.extra_tags)
        if tags:
            record.msg = '{0} | {1}'.format(
                record.msg,
                json.dumps(tags)
            )
        return logging.Formatter.format(self, record)
