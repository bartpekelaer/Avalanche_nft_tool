"""
logging.py

Logging functionality

"""


__author__ = ""
__version__ = "0.1.0"
__licence__ = "MIT"

# Standard Library Imports
import logging
import logging.config
import os
import yaml
import time

# 3rd Party Library Imports

# Local Module Imports

# Global Constants

# Global Variables

# Global Initializations

# Classes

# Functions
def setup_logging(default_path='\config\logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    
    Args:
        default_path (str): Default logging configuration file path.
        default_level (int): Default logging level.
        env_key (str): Enviroment variable key for logging configureration file path.
        
    Returns:
        None
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        

def get_logger(name):
    """Get logger instance
    
    Arges: 
        name (str): Logger name
        
    Returns:
        logger (Logger): Logger instance
    """
    
    logger = logging.getLogger(name)
    return logger


def log_exec_time(func):
    """Decorator that logs the execution time of a function.

    This decorator logs the execution time of a function using the `logging` module.
    It also adds a log message before and after the function execution, indicating
    that the function is being executed and when it's done executing.

    Example usage:

        @log_execution_time
        def my_function():
            # code here

    This will log the execution time of `my_function` using the `logging` module.
    """
    def wrapper(*args, **kwargs):
        logging.info(f'Executing {func.__name__}...')
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        final_time = end_time - start_time
        logging.info(f'Done in {final_time:.2f} seconds.')
        return result
    return wrapper

# Run