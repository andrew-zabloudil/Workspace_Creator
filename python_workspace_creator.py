#! python3

import os
import subprocess
import sys

"""
This program will automatically setup a new workspace for a new project.
It will create a new directory with the user's name of choice.
Then it will create a virtual environment within that directory.
It will activate the virtual environment and upgrade pip.
It will then install pylint and autopep8.
Finally, it will create a python file with the user's name of choice.
"""

# Uses a directory specified in environment variables for privacy.
WORKSPACE_DIRECTORY = os.getenv('WORKSPACE_DIRECTORY')


"""
Creates a new workspace folder, creates a virtual environment within it,
updates pip, and installs pylint and autopep8 before finally creating
a blank python file.
"""


def create_workspace(workspace_name='New_Workspace', file_name='main'):

    os.chdir(WORKSPACE_DIRECTORY)
    subprocess.run(f'mkdir {workspace_name}', shell=True)
    os.chdir(f'{WORKSPACE_DIRECTORY}\\{workspace_name}')
    subprocess.run('python -m venv venv')
    activate = '.\\venv\\Scripts\\Activate'
    venv_setup = f'{activate} && python -m pip install --upgrade pip && pip install pylint && pip install autopep8'
    subprocess.run(venv_setup, shell=True)
    subprocess.run(f'type nul > {file_name}.py', shell=True)


# Determines how many arguments to pass to the function from the command line.
if len(sys.argv) == 1:
    print(sys.argv)
    create_workspace()
elif len(sys.argv) == 2:
    print(sys.argv)
    create_workspace(sys.argv[1])
else:
    print(sys.argv)
    create_workspace(sys.argv[1], sys.argv[2])
