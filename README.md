# python-selenium-mock-up :rocket:
a mock up of how our automation solution would look like in python (condensed)

python 3.6.4

## To Use:

$ mkdir python-automation

$ cd python-automation

$ git clone git https://github.com/neuralhalation/python-selenium-mock-up.git

### Setup:

- install required modules with `pip install -r requirements.txt`

- Change the config.ini.sample file to config.ini, and add your configuration values (chromedriver path, site URL, login credentials)  








Start a virtualenv and make sure selenium is installed w/: $ pip install selenium 

Timing is still an issue in the application at the time of writing, so the solution suffers from not being able to get reliable load
times out of the application under test. 

credit for pagefactory_support goes to https://jeremykao.wordpress.com/2015/06/10/pagefactory-pattern-in-python/
