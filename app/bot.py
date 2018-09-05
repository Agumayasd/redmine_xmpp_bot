import multiprocessing as mp
import yaml
import time
import argparse


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class EmptyConfigFile(Error):
    """Exception raised when config file is emtpy

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


def fbot(project):
    while True:
        time.sleep(1)
        print('Send notification for project {0}'.format(project))


def getProjectConfig(stream, project):
    """
    This function get a project configuration
    from a YAML stream
    """

    try:
        # Load configuration file
        config = yaml.load(stream)

        # Check if stream is empty
        if config is None:
            message = 'config file is empty'
            raise EmptyConfigFile(message)
    except EmptyConfigFile:
        print('coucou')
        raise

    for i, v in enumerate(config):
        if project == v.get('project'):
            return v


def openConfigFile(file):
    """
    This function check configuration file syntax
    and return a stream
    """
    try:
        # Open configuration file
        with open(file, 'r') as f:
            config = yaml.load(f)
        if config is None:
            message = 'config file is empty'
            raise EmptyConfigFile(message)
    except yaml.YAMLError as exc:
        print("Error in configuration file:", exc)
        raise
    else:
        return config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage redmine bots')
    parser.add_argument('--redmine-project',
                        dest='redmineProject',
                        action='store',
                        required=True,
                        help='a redmine project name')
    args = parser.parse_args()
    getConfig(args.redmineProject)
