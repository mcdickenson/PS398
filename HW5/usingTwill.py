from twill import get_browser
b=get_browser()

from twill.commands import *
go("http://www.python.org/")
b.showforms()
b.showlinks()

# follow

