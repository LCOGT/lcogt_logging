#!/usr/bin/env python

'''
Tests for LCOGTFormatter. Requires libraries in requirements-tests.txt

Austin Riba
Aug 2015
'''

import sys
import logging
from testfixtures import log_capture
from lcogt_logging import LCOGTFormatter


class TestLogging(object):
    def get_logger(self, formatter=LCOGTFormatter()):
        logger = logging.getLogger()
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        return logger

    @log_capture()
    def test_simple_log(self, l):
        logger = self.get_logger()
        logger.error('simple log')
        assert 'simple log' in l.records[0].message

    @log_capture()
    def test_extra_tags(self, l):
        helpful_info = {'test': True, 'prod': False}
        logger = self.get_logger(LCOGTFormatter(extra_tags=helpful_info))
        logger.error('extra tags')
        assert all([_ in l.records[0].message for _ in ['extra tags',
                                                        '"test": true',
                                                        '"prod": false']])

    @log_capture()
    def test_logger_tags(self, l):
        logger = self.get_logger()
        logger.error('log level tags', extra={"tags": {"foo": "bar"}})
        logger.error('this omits tags')
        assert all([_ in l.records[0].message for _ in ['log level tags',
                                                        '"foo": "bar"']])
        assert 'this omits tags' in l.records[1].message
        assert 'foo' not in l.records[1].message

    @log_capture()
    def test_logger_and_extra_tags(self, l):
        helpful_info = {'test': True, 'prod': False}
        logger = self.get_logger(LCOGTFormatter(extra_tags=helpful_info))
        logger.error('this has it all', extra={"tags": {"foo": "bar"}})
        assert all([_ in l.records[0].message for _ in ['this has it all',
                                                        '"test": true',
                                                        '"prod": false',
                                                        '"foo": "bar"']])
