from twill import get_browser
b=get_browser()

from twill.commands import *
go("http://www.python.org/")
b.showforms()   
b.showlinks()   # all pages linked to by all pages in history
show()        # show page source (HTML)

# http://twill.idyll.org/commands.html
# follow

