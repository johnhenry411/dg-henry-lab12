import logging

# Constants for logger names
ROOT_LOGGER = 'RootLogger'
LOGGER1_NAME = 'Logger1'
LOGGER2_NAME = 'Logger2'

try:
    # Configure the root logger
    logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s - %(asctime)s', level=logging.INFO)

except Exception as e:
    print(f"Error configuring logging: {e}")

# Create additional loggers
logging.getLogger(ROOT_LOGGER).setLevel(logging.INFO)
logger1 = logging.getLogger(LOGGER1_NAME)
logger2 = logging.getLogger(LOGGER2_NAME)

# Set different levels for each logger
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.WARNING)

# Add file handler to root logger
file_handler = logging.FileHandler('your_log_file.log')
file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s - %(asctime)s'))
logging.getLogger(ROOT_LOGGER).addHandler(file_handler)

# Log messages using different loggers
logging.info("This message uses the root logger and will be logged.")
logger1.debug("This message uses Logger1 and includes detailed debugging information.")
logger2.warning("This message uses Logger2 and warns about a potential issue.")
