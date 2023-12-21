# Community Code - Web - Python Starter Project
This project demonstrates how to write tests for Continuous Testing Cloud using Python. Once cloned and set up properly, it runs as is.

## Setting Up the Sample Project

1. Clone the sample project.
    ```bash
    git clone https://github.com/ExperitestOfficial/CommunityCode-Web-PythonStarterProject
    cd CommunityCode-Web-PythonStarterProject
    ```
1. Set up authentication by updating these  parameters in [cloud.properties](cloud.properties):
    * url - URL for the cloud to run the test in. For example, https://company.digitai.ai/
    * accessKey -  Personal authentication. See [Obtaining Access Key](https://docs.digital.ai/bundle/TE/page/obtaining_access_key.html) to learn how to obtain an access key.
1. Make sure that Python 3 is installed.
1. Install the dependencies.
```bash
pip install -r requirements.txt
```

## Running Tests
To run all tests in this project, run this on the command line: 

```bash
python -m unittest
```

## Desired Capabilities
In this example we use browser options to run a test on Chrome. Import a different browser options class to run your test on a different browser.

```
from selenium.webdriver.chrome.options import Options
```

Continuous Cloud Testing expands Selenium's capabilities and allows better control over the device and test.
See [Capabilities in Selenium Tests](https://docs.digital.ai/bundle/TE/page/capabilities_in_selenium_tests.html) to learn how to customize the desired capabilities for your tests.

## Documentation
To find out more about Continuous Cloud Testing usage, features, and best practices, see our online [documentation](https://docs.digital.ai/bundle/TE/page/test_execution_home.html).

## Support
If you encounter an issue that is not covered here or in our online documentation, contact us at [support@digital.ai](mailto:support@digital.ai).
