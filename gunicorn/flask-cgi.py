#
# Flaskアプリケーションを CGI で動かすサンプルです.
#
import cgitb
from wsgiref.handlers import CGIHandler
from myapp import app

cgitb.enable()
CGIHandler.run(app)
