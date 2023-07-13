# OrangeHRM_Automation
 
This is a portfolio demo Automation project.

Libraries: Playwright, PyTest

Tools: Python

Implemented Design Patterns: POM & PyTest Fixtures.


Test Data: Test Data is stored in dedicated json files here: src/tests/test_data/user_data.json We can choose which test data file to use in our executions by using the following command: " pytest --datafile=[path]/[data-file-name]" 
For example : pytest --datafile=src/tests/test_data/user_data.json

Debugging: Playwright traces are recorded and also loggers were added in critical places.

How to execute test suites? 
Please make sure you're in the root directory of the project and run the following command: "make [suite-name]"
For example: "make sanity-tests"

