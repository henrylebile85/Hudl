# Run on Local machine#
- Clone Repository  
- Activate Virtual environment  
- Install dependencies  
- Set Environment Variables
- Run tests and generate report 
- Check test reports  

## Clone Repository
on the cmd, Run   
git clone https://github.com/henrylebile85/Hudl.git  

Navigate to the cloned project   
cd hudl  

## Setting up a new Virtual environment or activating the Virtual environment within the project
- Activate the Virtual Environment within the hudl project venv (venv_hudl) 
  Execute command from the hudl project   

  - Windows {bash}(Command Prompt): 
    venv_hudl\Scripts\activate  

  - Windows (PowerShell): 
    venv_hudl\Scripts\Activate.ps1  

  - Mac/Linux(bash) 
    source venv_hudl/bin/activate    

- Deactivate the Virtual Environment   
  deactivate 

- Create a Virtual Environment 
  python -m venv virtual_environment_name 
  Note: command for python 3 and above 


## Install dependencies  
- Confirm if dependencies are already installed   

  pip freeze from the venv_hudl virtual environment or from the newly created virtual environment   
  
  If dependencies are installed, proceed to setting the environment variables  

- Install dependencies 

  If dependencies are not installed, re-install them from the requirements.txt file   

  pip install -r requirements.txt   

Note: If you create a new virtual environment, you would need to install all the dependencies from the 
requirements.txt file 

## Set Environment Variables
- Set Browser environment variable to select the desired browser to run the test 
  - For windows use any of the following, depending on the browser you want to run (no spaces in *=* )   
    set BROWSER=chrome  
    set BROWSER=firefox   

  - For apple use any of the following, depending on the browser you want to run (no spaces in *=* )   
    export BROWSER=chrome
    export BROWSER=firefox
    export BROWSER=safari   

- Set EnvironmentI (Not required)
  - prod is set as the default value. 
    For the purpose of this Hudl exercise, we would be using only prod  

- 📌 **(Optional):** Set html Report Directory 
  - For windows use any of the following, (no spaces in *=* )   
    set RESULTS_DIR=then enter the absolute path of where you want the file to be stored e.g. reports   

  - For apple use any of the following, depending on what browser you want to run (no spaces in *=* )   
    export RESULTS_DIR=then enter the absolute path of where you want the file to be stored e.g. reports   


## Run Test and Generate Reports  
- Navigate to the hudl package   
  cd hudl   

- Execute tests from the hudl package  
  Run command   
  pytest -m login -n auto --html=Reports/report.html --self-contained-html   

## Check Test Reports 
- Default location   
  Reports are located in the hudl package under Reports
  😊 your current directory  

- Environment Variable location 
  the reports would be located 📌 **(here):** the absolute path of where you want the file to be stored 


### Additional information
- Dependencies 
  - Selenium 
  - pytest 
  - pytest-xdist 
  - pytest-html
  - webdriver-manager
  

  


