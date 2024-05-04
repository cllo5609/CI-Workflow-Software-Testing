# CI-Workflow-Software-Testing
This repository houses the code and documentation for the group portfolio project created as part of the CS 362 - Software Engineer II course work at Oregon State University.

## Motivation
The purpose of this project is to design, implement, and demonstrate a Continuous Integration Workflow, mimicking that practiced in professional software development environments. Development techniques and methodologies used include:
* Applying automated tools such as make, CVS, flake8 linter, and GitHub Actions in a realistic setting
* Applying testing techniques for validating and measuring the quality of software
* Using Branch Rules to set requirements for merging changes
* Using appropriate techniques and tools, including a debugger, to locate program faults
* Participating effectively in software inspection/code reviews
* Participating effectively in a team environment

## Workflow Setup
The Continuous Integration Workflow for this project was established using GitHub Actions. Using the Python application workflow provided by GitHub, we were able to modify the produced YML file to configure the project workflow. This workflow monitors changes to all branches that are pushed to the repo and runs the build process for each branch. This allows developers to see if their changes will fail the build before requesting a pull request into main. 

Once triggered, this action will look under the jobs field and begin executing the 'build' job which initiates a Ununtu virtual machine that follows the steps defined under the 'steps' field. Once the virtual machine is set up, the workflow will run a linter on the code to identify any syntax and style issues. If the linter finds problems in the code, the build is stopped and the workflow fails.

The workflow then runs the custom test suite 'tests.py', executing a series of unit tests on the functions defined in the 'task.py' file. This will result in either a successful or failed build.

## Branch Rules
To prevent direct changes to the main branch of the repository, a branch protection rule was created. This branch rule requires collaborators, excluding administrators, to create a new branch to make changes and then push the branch to GitHub. This push triggers the workflow, and GitHub will attempt to build the server. 

If the build is successful, developers can initiate a pull request to have that branch merged into main. Before a branch can be merged into main, the changes must be reviewed and approved by one other collaborator by completing a code review on the requested changes.

## task.py
The task.py file houses the code for three functions. Each team member was tasked with implementing one of the three functions. By each working from the same file, encountering and handling merge conflicts were common. The functions were designed and implemented based on the specifications listed below:

### Function 1 Specification
This function must have the following header: def conv_num(num_str). This function takes in a string and converts it into a base 10 number, and returns it. It has the following specifications:

* Must be able to handle strings that represent integers
* Must be able to handle strings that represent floating-point numbers
* Must be able to handle hexadecimal numbers with the prefix 0x
  - Must be case insensitive
  - Negative numbers are indicated with a - like -0xFF
  - Only integers are valid inputs for hexadecimal numbers (i.e., no 0xFF.02)
* The type returned must match the type sent. For example, if a string of an integer is passed in, conv_num must return an int.
* Invalid formats should return None (n.b. this is not a string, but the actual None value), including, but not limited to:
  - strings with multiple decimal points
  - strings with alpha that aren't part of a hexadecimal number
  - strings with a hexadecimal number without the proceeding 0x
  - values for num_str that are not strings or are empty strings

### Function 2 Specification
This function must have the following header: def my_datetime(num_sec). This function takes in an integer value that represents the number of seconds since the epoch: January 1st, 1970. The function takes num_sec and converts it to a date and returns it as a string with the following format: MM-DD-YYYY. It has the following specifications:

* It may be assumed that num_sec will always be an int value
* It may be assumed that num_sec will always be a non-negative value
* Must be able to handle leap years
  
### Function 3 Specification
This function must have the following header: def conv_endian(num, endian='big'). This function takes in an integer value as num and converts it to a hexadecimal number. The endian type is determined by the flag endian. The function will return the converted number as a string. It has the following specifications:

* It may be assumed that num will always be an integer
* Must be able to handle negative values for num
* A value of big for endian will return a hexadecimal number that is big-endian
* A value of little for endian will return a hexadecimal number that is little-endian
* Any other values of endian will return None (n.b. this is not a string, but the actual None value)
* The returned string will have each byte separated by a space
* Each byte must be two characters in length
