This program sets up a workspace for a new Python project. It is currently set up to run from a PowerShell script, but can be modified fairly easily.

Required setup:
    You must have an appropriately named environment variable ("WORKSPACE_DIRECTORY") pointing to the directory you wish to create the new project in.

What this program does:
    First, it creates a new subdirectory in the directory pointed to by the WORKSPACE_DIRECTORY environment variable.
    Next, it creates a python virtual environment within that subdirectory.
    Once the virtual environment has been created, the program will update pip, install pylint, and install autopep8.
    Finally, the program will create a blank python file.

The program takes up to two arguments when run from PowerShell. The first argument specifies the name of the subdirectory (Default: "New_Workspace"), and the second specifies the name of the blank python file with no file extension (Default: "main", creates "main.py").