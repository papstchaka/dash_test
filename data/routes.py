#####################################################################################################################
## imports

from data.server import server
from data.home import app as _home
from data.project import app as _project

#####################################################################################################################
## home site
@server.route("/")
def home():
    return _home ## return home-app

## project site
@server.route("/project/") ## needs to be changed if name of project subwebsite is not "project"
def project():
    return _project ## return "project"-app