from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
import unittest, time, re, datetime, os, random, traceback
import sys, argparse, optparse, pyodbc, inspect
import SeleniumTestHelper 
from SeleniumTestHelper import SeleniumTestHelperTwo
from testconfig import config



option = SeleniumTestHelper.env_variable
config = SeleniumTestHelper.SeleniumTestHelperTwo.environment_setter(option)
