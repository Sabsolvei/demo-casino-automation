<div>
    <h1 align="center">DEMO CASINO </h1>
<h2 align="center">AUTOMATION</h2>
<hr/>
    <p> 
        Project to automate User Registration and an additional feature of the DEMO.CASINO website. 
        This covers just a few test cases of each feature as sample. 
        The frameworks used are Selenium+Python, Pytest, which allows flexible setting of the tests, and Allure to 
        provide a detailed report of executions results.
    </p>
</div>
<hr/>

### Get started

#### Install Requirements

- [`PYTHON 3.7+`](https://www.python.org/downloads/) 

1. Create the **'virtual environment'** in project's root directory.  
**Specify the python version in case you have more than one version installed.*

```commandline
py -3.10-64 -m venv venv
```


2. Activate the **'virtual environment'**

```commandline
 . venv/Scripts/activate
```

3. Instal all requirements from ***'requirements.txt'*** file
    
```commandline
pip3.10 install -r requirements.txt
```

---
### Tests Execution

`selenium_pytest_demo/tests` directory contains all test suites.  


**Main Command lines:**

>**Custom commandline options**  
> -B / --browser : ['chrome', 'firefox', 'edge', 'all']  
> -m : ['smoke', 'regression'] 
> 
> *-h : help for more options*

1. Run all tests
```commandline
pytest --alluredir=reports
```  

2. Run specific suite test
```commandline
pytest -v --alluredir=reports home_tests.py
```

3. Run specific testing type  
```commandline
pytest -v -m "smoke"
```
```commandline
pytest -v -m "not regression"
```

---
### Reports review
Adding --alluredir option to commandline enable Allure to store results in the provided path.  
**To see the actual report execute from the commandline:**
```commandline
allure serve ./reports
```
This command will show you generated report in your default browser.  
`localhost:port`