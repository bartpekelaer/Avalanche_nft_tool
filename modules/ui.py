"""
ui.py

User Interface
"""


__author__ = ""
__version__ = "0.1.0"
__licence__ = "MIT"

# Standard Library Imports
import tkinter
import yaml

# 3rd Party Library Imports

# Local Module Imports

# Global Constants
with open('./config/config.yaml', 'r') as f:
    ui_config = yaml.safe_load(f)
    
window_name = ui_config['ui']['window_name']
window_width = ui_config['ui']['window_width']
window_height = ui_config['ui']['window_height']
bg = ui_config['ui']['bg']
text_col = ui_config['ui']['text']
font = ui_config['ui']['font']
font_size = ui_config['ui']['font_size']

# Global Variables

# Global Initializations

# Classes

# Functions

# Run