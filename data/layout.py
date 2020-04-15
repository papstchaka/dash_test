#####################################################################################################################
## imports  

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc ##has some nice other elements for html and bootstrap objects

#####################################################################################################################
## layout class for dash-frontend
class layout():

    #####################################################################################################################
    ## inits the class
    ## title = Title of Sites (default="" // String) || project_name = name of project-url (sets url and stuff) (default="" // String) || home_header = header on home website (default="" // String) || home_dropdown_options = options in dropdown on home website (default=[] // List) || home_dropdown_placeholder = placeholder for dropdown on home website (default="" // String)
    def __init__(self,title="",project_name="",home_header="",home_dropdown_options=[],home_dropdown_placeholder=""):
        self.title = "Titel" if title == "" else title ##sets title
        self.project_name = "project" if project_name == "" else project_name ##sets name of project
        self.home_header = "Home Header" if home_header == "" else home_header ##sets header of home-website
        self.home_dropdown_options = ["Home Dropdown Option 1"] if home_dropdown_options == [] else home_dropdown_options ##sets dropdown options on home site
        self.home_dropdown_placeholder = "Home Dropdown Placeholder" if home_dropdown_placeholder == "" else home_dropdown_placeholder ##sets placeholder for dropdown on home site


        ##import external js-scripts for dash app
        self.external_scripts = []
        ##import external css-stylesheets for dash app
        self.external_stylesheets = ['/static/css/style.css', '/static/css/button.css', 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css', '/static/css/dropdown.css']
        
    #####################################################################################################################
    ## sets layout
    ## site = subsite that shall be displayed ("index" (default) = raw, empty site needed for "display-page"-callback in project.py / "home" = home-site / <project_name> = projects-site // String)
    ## return html-Div with whole layout
    def layout(self,site="index"):

        home="-active" if site == "home" else "" ##just sets the shadow on the Sidebar-options
        project="" if site == "home" else "-active" ##just sets the shadow on the Sidebar-options

        #####################################################################################################################
        ##init list of html-layout elements
        layout_list = [
            
        #####################################################################################################################
        ## Navbar
            html.Nav([
                html.Ul([
                    html.Li(
                        html.A("Startseite", href="/", className="cta-btn cta-btn--resume"+home)
                        ),
                    html.Li(
                        html.A(self.project_name[0].upper()+self.project_name[1:].lower(), href="/"+self.project_name.lower()+"/", className="cta-btn cta-btn--resume"+project)
                        ),
                    html.Li(
                        html.Form(
                            dcc.Input(
                                id="Search-Content", placeholder="Search", n_submit=0, type="search", className="form-control mr-sm-2")
                        ,method="GET",className="cta-btn cta-btn--resume")
                    ,className="_push")
                ],className="main-navigation")
            ],className="zone hero sticky"), ##NavBar
        ]
        #####################################################################################################################
        ## content

        #####################################################################################################################
        ## home website
        if site == "home":
            ##extend the list of layout elements however you want
            #####################################################################################################################
            ## inner-content
            layout_list.extend([
                dcc.Location(id="url", refresh=True),
                html.Div([
                    html.Div(
                            html.H2(self.home_header,className="sub-header") ##Sub-Heading
                    ,className="navbar navbar-expand-lg navbar-light centered"
                    ), ##Div to sort the sub-heading
                #####################################################################################################################
                ## Dropdowns
                    html.Nav(
                        html.Div(
                            dcc.Dropdown(id="dropdown",options=[{'label':name,'value':name} for name in self.home_dropdown_options],placeholder=self.home_dropdown_placeholder)
                        ,className="nav-link mydropdown-toggle") ##dropdown for home-site
                    ,className="navbar navbar-expand-lg navbar-light centered"
                    ),           
                #####################################################################################################################
                ## all other html components

                            ## to be continued
                            ## add more html elements
                
                #####################################################################################################################
                ],className="mycontainer white zone") ##Div for whole inner content
            ])
        
        #####################################################################################################################
        ## <project_name> website
        elif site == self.project_name.lower():
            ##extend the list of layout elements however you want
            #####################################################################################################################
            ## inner-content
            layout_list.append(
                html.Div([
                    #####################################################################################################################
                    ## Dropdowns
                        html.Nav(
                            html.Div(
                                dcc.Dropdown(id="dropdown",options=[{'label':name,'value':name} for name in self.home_dropdown_options],placeholder=self.home_dropdown_placeholder)
                            ,className="nav-link mydropdown-toggle") ##dropdown for home-site
                        ,className="navbar navbar-expand-lg navbar-light centered"
                        ),          
                    #####################################################################################################################
                                
                    #####################################################################################################################
                        html.Div([
                            dcc.Markdown(id="text1", style={"margin-top": "1rem","white-space":"pre-line"}),
                            dcc.Markdown(id="text2", style={"margin-top": "1rem","white-space":"pre-line"}),
                            dcc.Markdown(id="text3", style={"margin-top": "1rem","white-space":"pre-line"}),
                        ],className="row has-shadow bg-white",style={"padding-left":"20px","padding-right":"20px"}), ##Div to sort the info
                    #####################################################################################################################
                ],className="mycontainer white zone") ##Div for whole inner content
            )

        ##more subwebsites possible with more elif statements
        
        #####################################################################################################################
        ## more stuff
        layout_list.extend([
            html.Div(""
                ## space for new stuff
            ,className="zone content grid-wrapper"),
        # #####################################################################################################################
        # ## footer
            html.Footer(
                html.A("[2020] Alexander Christoph", href="https://github.com/papstchaka", target="_blank", className="signature cta-btn cta-btn--resume-active _push")
            ,className="footer main main-navigation")
        ])

        #####################################################################################################################
        ## index site // an "empty" webiste that contains all html elements (but hidden, so not seen)
        ##      you will need an index site with all html and dcc elements that are called by one of the running apps (in home.py and project.py)
        ##      --> every element that causes a callback (as Input or Output) --> they should be hidden by 'style={"display":"none"}' to avoid unwanted interferences
        if site == "index":
            layout_list = [
                dcc.Location(id="url", refresh=True), ## Location object to change the url
                dcc.Location(id="sub-url", refresh=True), ## Location object to change the url for subwebsites search
                html.Div(id='page-content'), ## Div object that holds layout
            ]  

        return html.Div(layout_list)