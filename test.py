import logging
from testfixtures import log_capture
import sys
from lcogt_logging import LCOGTFormatter


class TestLogging:
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
        l.check(
            ('root', 'ERROR',  'simple log')
        )

    @log_capture()
    def test_extra_tags(self, l):
        helpful_info = {'test': True, 'prod': False}
        logger = self.get_logger(LCOGTFormatter(extra_tags=helpful_info))
        logger.error('extra tags')
        l.check(
            ('root', 'ERROR', 'extra tags | {"test": true, "prod": false}')
        )

    @log_capture()
    def test_logger_tags(self, l):
        logger = self.get_logger()
        logger.error('log level tags', extra={"tags": {"foo": "bar"}})
        logger.error('this omits tags')
        l.check(
            ('root', 'ERROR', 'log level tags | {"foo": "bar"}'),
            ('root', 'ERROR', 'this omits tags')
        )
