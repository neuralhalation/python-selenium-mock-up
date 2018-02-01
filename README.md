# python-selenium-mock-up
a mock up of how our automation solution would look like in python (condensed)

python 2.7.4

to use go to terminal: 

$ mkdir python-automation

$ cd python-automation

$ git clone git https://github.com/neuralhalation/python-selenium-mock-up.git


Open up test_basic.py and replace the setup path to your local instance of chromedriver.exe

I recommend putting chromedriver right in with your python-automation folder just created

Change the config.ini.sample file to config.ini, and add your configuration values

Start a virtualenv and make sure selenium is installed w/: $ pip install selenium 

Timing is still an issue in the application at the time of writing, so the solution suffers from not being able to get reliable load
times out of the application under test. 

credit for pagefactory_support goes to https://jeremykao.wordpress.com/2015/06/10/pagefactory-pattern-in-python/
