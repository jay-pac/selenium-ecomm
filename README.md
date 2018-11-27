## Ecomm Selenium Project
This project is written in python and serves an example of implementing a Selenium framework against an ecomm site. The design pattern being used is a Page Object Model.  POM is used to have reusable WebElements/small helper methods separated from the actual test classes, allowing for cleaner code and easier test maintenance.

### Getting Started
1. Install Python 3.x
https://www.python.org/downloads/  
*Optionally, you can create a virtual env to isolate Python dependencies between projects*

2. In a terminal install the following packages:  
`pip install selenium`  
`pip install pytest`  
3. Clone repo to your local machine

### Running Tests
To execute the tests just browse to the path where the selenium project is located in your terminal and type:
`py.test tests/home/login_tests.py`
*If no browser is specified, Chrome is used by default*  

use `--browser <browser_name>` to specify which browser to test against:  
`py.test tests/home/login_tests.py --browser firefox`  

### Logs
Log files are created with each test and if the test fails a screenshots is taken to  provide further information about what happened if they failed. The screenshots reside in the ./screenshots directory and can be viewed locally in your IDE
