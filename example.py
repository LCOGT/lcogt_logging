import sys
import os
import logging
from lcogt_logging import LCOGTFormatter

# Get a named logger
logger = logging.getLogger('example')

# Define some constants we want added to every log
helpful_info = {'example': True, 'pid': os.getpid()}

# Instantiate our LCOGTFormatter, passing in the info dict
formatter = LCOGTFormatter(extra_tags=helpful_info)

# Define a StreamHandler - handles where the log is written, at what level
# and what format
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)


# Add the handler to the logger, which is now ready to use.
logger.addHandler(stream_handler)

# A simple log
logger.error("Starting the example")

# A log with additional tags
logger.critical("Log with additional tags", extra={"tags": {"foo": "bar"}})

# Recreate the formatter, but with no extra tags for sparse logs.
formatter = LCOGTFormatter()
stream_handler.setFormatter(formatter)
logger.warn("Log with no tags at all")
