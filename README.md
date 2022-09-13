<div>
    <h1 align="center">DEMO CASINO </h1>
<h2 align="center">AUTOMATION</h2>
<hr/>
    <p> 
        Project to automate User Registration and an additional feature of the DEMO.CASINO website. 
        This covers the most relevant test cases of each feature. 
        The frameworks used are Selenium+Python, Pytest, which allows flexible setting of the tests, and Allure to 
        provide a detailed report or executions results.
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

Several tests are marked as **smoke**, **sanity**  and **regression**. This allows you to choose which type of testing to perform

**Main Command lines:**

1. Run all tests
```commandline
pytest -v
```  

2. Run specific suite test
```commandline
pytest -v home_tests.py
```

3. Run specific testing type
```commandline
pytest -v -m "smoke"
```
```commandline
pytest -v -m "not regression"
```
```commandline
pytest -v -m "not regression" home_tests.py
```
