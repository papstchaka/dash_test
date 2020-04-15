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
                routes_pathname_prefix="/"+layout.project_name.lower()+"/")
app.config['suppress_callback_exceptions']=True

#####################################################################################################################
## set up layout
app.title = layout.title ##set title
app.layout = layout.layout ##set index layout (is needed for the "display-page" - callback)

## initial call of backend
b = backend()

#####################################################################################################################
## Search callback
@app.callback(Output('sub-url',"pathname"),[Input('Search-Content', 'n_submit'),Input('Search-Content', 'value')]) ##change the url in dependence of the elected value in the SearchField
def redirect(n_submits=0, content=None):
    if n_submits > 0 and content != None:
        return content

#####################################################################################################################
## Home callbacks that subsite is even displayed
@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')]) ## changes websites-layout in dependence of the given url
def display_page(pathname = None):
    if pathname is not None: ##if url is changed
        return layout.layout(layout.project_name.lower()) ##return subwebsites layout    
    return layout.layout("home") ##otherwise return homesite layout

@app.callback([Output('text1', 'children'),Output('text2', 'children'),Output('text3', 'children')],[Input('url', 'pathname'),Input("dropdown", "value")])
def test1(new_url,dropdown):
    
    return "text1", "text2", "text3"