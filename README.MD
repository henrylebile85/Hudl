#Run on Local machine#

***Activate the Virtual Environment***
Execute command from the hudl project

-Windows {bash}(Command Prompt):
venv_hudl\Scripts\activate

-Windows (PowerShell):
venv_hudl\Scripts\Activate.ps1

-Mac/Linux(bash)
source venv_hudl/bin/activate


***Confirm dependencies are installed***
pip freeze from the venv_hudl virtual environment
If dependencies are not installed, re-install them from the requirements.txt file
pip install -r requirements.txt

Note: If you create a new virtual environment, you would need to download all the dependencies from the requirements.txt file


***Set Environment Variables***
Windows


Mac



***Run command in cmd to run the test and generate reports***
pytest -m login_test --html=report.html --self-contained-html --title="Hudl login test"


***Generating HTML Reports with pytest-html***
pytest-html is a plugin for pytest that allows you to generate an HTML test report, making it easier to analyze test results.
Add Self-contained Report (Includes CSS & JS inline):
pytest --html=report.html --self-contained-html
Set a Custom Report Title:
pytest --html=report.html --self-contained-html --title="Hudl login test"



# hudl-login-tests

A brief description of what the project does and why it’s useful.

## Installation

Instructions for installing and setting up the project.

## Usage for local cloning
How to use the project, with examples if necessary.

## Usage for runing through git actions
How to Manually Run the Workflow and execute tests from GitHub.    
Go to GitHub → Actions.   
Select "Run Hudl UI Tests Securely" from the list.  
Click "Run workflow".  
The tests will execute immediately.  

## Contributing

Guidelines for contributing to the project.

## License

Information about the project’s license.


