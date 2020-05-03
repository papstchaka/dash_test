# dash_test
Short Implementation that shows how plotly-dash can be used as framework to host webistes that are created with basic HTML + CSS using a flask server.

<h2 align="center">
  <img src=https://github.com/papstchaka/dash_test/blob/master/data/static/assets/index.jpg alt="Home View" width="800px" />
</h2>

## Requirements
* flask
* dash
* dash_core_components
* dash_html_components
* dash_bootstrap_components (not yet used in implementation but imported in `data/layout.py`)
> install via `pip install flask dash dash_core_components dash_html_components dash_bootstrap_components`

## Fork project and set it up to work on local laptop
* Fork/Clone the repository to your local machine into a folder like `dash_test`, go to that folder and run `python start.py`. 2222 is the projects default backend port. Of course you can change that if you want by changing `server.run(debug=True,port=<desired_port>,host="localhost")` in `data/start.py`
* head to `localhost:<desired_port>` to see the frontend

## Functionality

App provides to 'different' sites that are already implemented:
* Index website
* one subsite
* both sites have a Search Option which does nothing more than changing the url (which won't change the output view if you are not typing in `project`)

* in `routes.py` / `home.py` / `project.py` you can see how routing can be done in dash using different dash apps
* in `layout.py` you can see how the layout - which is almost similar to the `html`-version in my <a href="https://github.com/papstchaka/django_test" target="_blank">django_test</a> repo - can be easily implemented without using any HTML or JavaScript, only with Python and some CSS - for styling reasons.
> Layout can be easily changed by changing the default variables in `layout.py`'s class header or adding other dash-objects

<h2 align="center">
  <img src=https://github.com/papstchaka/dash_test/blob/master/data/static/assets/subsite.jpg alt="Subsite View" width="800px" />
</h2>
