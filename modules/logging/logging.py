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

# Run