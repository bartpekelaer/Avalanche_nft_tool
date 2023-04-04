"""
database.py

This module contains functions for interacting with a SQLite3 database using the `sqlite3` module.

Functions:
- with_commit(function): A decorator function that adds a commit after a function is executed.
- build(): Executes a script file called "BUILD" if it exists and commits the changes.
- commit(): Commits the changes made to the database connection.
- autosave(schedule): Adds a job to the provided schedule to commit changes to the database connection on a regular interval.
- close(): Closes the database connection.
- field(command, *values): Executes a SQL command that returns a single value and returns that value.
- column(command, *values): Executes a SQL command that returns a column of values and returns a list containing those values.
- record(command, *values): Executes a SQL command that returns a single row of values and returns that row.
- records(command, *values): Executes a SQL command that returns multiple rows of values and returns all of those rows.
- execute(command, *values): Executes a SQL command without returning any values.
- multiexec(command, *valueset): Executes a SQL command multiple times with different sets of values.
- scriptexec(path): Executes a script file at the provided path.
"""


__author__ = ""
__version__ = "0.1.0"
__licence__ = "MIT"

# Standard Library Imports
from os.path import isfile
from sqlite3 import connect

# 3rd Party Library Imports
from apscheduler.triggers.cron import CronTrigger

# Local Module Imports

# Global Constants
DATABASE = 'database/sqlite3/database.sqlite3'
BUILD = 'database/build.sql'

# Global Variables

# Global Initializations
cxn = connect(DATABASE, check_same_thread=False)
cur = cxn.cursor()

# Classes

# Functions
def with_commit(function):
    """A decorator function that adds a commit after a function is executed.
    """
    def inner(*args, **kwargs):
        function(*args, **kwargs)
        commit()
        
    return inner


@with_commit
def build():
    """Executes a script file called "BUILD" if it exists and commits the changes.
    """
    if isfile(BUILD):
        scriptexec(BUILD)


def commit():
    """Commits the changes made to the database connection.
    """
    cxn.commit()


def autosave(schedule):
    """Adds a job to the provided schedule to commit changes to the database connection on a regular interval.
    
    :param schedule: A schedule object for scheduling jobs.
    """
    schedule.add_job(commit, CronTrigger(second=0))
    

def close():
    """Closes the database connection.
    """
    cxn.close()


def field(command, *values):
    """Executes a SQL command that returns a single value and returns that value.
    
    :param command: A string containing a valid SQL command.
    :param values: The values to be passed to the SQL command.
    :return: The first value returned by the SQL command.
    """
    cur.ex
    cur.execute(command, tuple(values))
    
    if (fetch := cur.fetchone()) is not None:
        return fetch[0]


def column(command, *values):
    """Executes a SQL command that returns a column of values and returns a list containing those values.
    
    :param command: A string containing a valid SQL command.
    :param values: The values to be passed to the SQL command.
    :return: A list of values returned by the SQL command.
    """
    cur.execute(command, tuple(values))
    
    return [item[0] for item in cur.fetchall()]
    

def record(command, *values):
    """Executes a SQL command that returns a single row of values and returns that row.
    
    :param command: A string containing a valid SQL command.
    :param values: The values to be passed to the SQL command.
    :return: The first row returned by the SQL command.
    """
    cur.execute(command, tuple(values))
    
    return cur.fetchone()   
    
    
def records(command, *values):
    """Executes a SQL command that returns multiple rows of values and returns all of those rows.
    
    :param command: A string containing a valid SQL command.
    :param values: The values to be passed to the SQL command.
    :return: A list of rows returned by the SQL command.
    """
    cur.execute(command, tuple(values))
    
    return cur.fetchall()


def execute(command, *values):
    """Executes a SQL command without returning any values.
    
    :param command: A string containing a valid SQL command.
    :param values: The values to be passed to the SQL command.
    """
    cur.execute(command, tuple(values))
    
    
def multiexec(command, *valueset):
    """Executes a SQL command multiple times with different sets of values.
    
    :param command: A string containing a valid SQL command.
    :param valueset: A set of values to be passed to the SQL command.
    """
    cur.executemany(command, valueset)
    

def scriptexec(path):
    """Executes a script file at the provided path.
    
    :param path: A string containing the path to the script file.
    """
    with open(path, 'r', encoding='utf-8') as script:
        cur.executescript(script.read())


# Run