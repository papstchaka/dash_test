#####################################################################################################################
## imports
from dash.dependencies import Input, Output, State
import dash

from data.backend import backend
from data.server import server
from data.layout import layout as _layout
#####################################################################################################################

layout = _layout() ##init layout

#####################################################################################################################
## set up the app with callbacks and stuff for specific subsite
app = dash.Dash(__name__,
                external_scripts=layout.external_scripts,
                external_stylesheets=layout.external_stylesheets,
                server=server,
                routes_pathname_prefix="/")
app.config['suppress_callback_exceptions']=True

#####################################################################################################################
## set up layout

app.title = layout.title ##set title
app.layout = layout.layout("home") ##set home layout

#####################################################################################################################
## Dropdown + Search callback
@app.callback(Output('url',"pathname"),[Input('dropdown', 'value'),Input('Search-Content', 'n_submit'),Input('Search-Content', 'value')]) ##change the url in dependence of the elected value in the dropdown and given Search-Input
def redirect(dropdown=None, n_submits=0, content=None):
    if dropdown != None: ##if dropdown value is changed
        return "/"+layout.project_name.lower()+"/"+dropdown.lower() ##return url to subwebsite with elected dropdown value
    if n_submits > 0 and content != None:
        return content

# @app.callback(Output(),[Input()])
# def to_be_continued():