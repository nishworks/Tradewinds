# Mandi - Managing grains

This is a an ambitious web app which aims to serve all the use cases in a grain market.

*Documentation*: http://mandi.readthedocs.org/en/latest/

## Setup Guide:
  * You should have these installed:  **python 2.7** and **pip**
  * **Tox Installation** (try with sudo if there is a permission error):
                ```
                pip install tox
                ```
    * Once you are in the project root directory and you have tox installed, execute
                ```
                tox
                ```
    * This will create a virtual environment under 'project_root/.tox' directory and will install all the python packages in it specified by requirement.txt.
  * **Activate virtual environment** - In the project root, execute
                ```
                source activate
                ```
  * **Starting the server** -
                ```
                python manage.py runserver
                ```
  * **Data-Store**:  We are going to use mysql for now.
  * **Dependencies:**
    * Python dependencies are specified in requirements.txt
    * Whenever a new package is added to requirements.txt, please add description/need for it here.
       * gunicorn -  Runs multiple instances of our Flask server (for scalability)
       * Flask - (The micro web-framework)
       * Flask-Script (Required for manage.py command CLI)
       * Flask-SQLAlchemy  (Useful utilities over SQL-Alchemy for use in Flask)
       * SQLAlchemy==1.0  (Object-Relational-Mapper)
       * ipython (Nice alternative to official python shell)
       * Jinja2  (Templating engine)
       * requests ( HTTP library)
       * sphinx (Documentation tool)
       * sphinx_rtd_theme (Theme for sphinx)


## Documentation
  * Documentation is rebuilt on readthedocs.org whenever a commit is pushed to this repository.


## Development Guide:

   * **Manage.py CLI**
       * Provides you with following commands:
           * runserver -  To run the development server with config defined in config.py
           * gunicorn -  To run multiple instances of the server for scalability
           * dirs - To list important directories configured in main app
           * config - To print out app config
           * routes - To list routes configured in an app
           * **Auto-Restart of server on code change:**
             * It's convenient to have server reload modified code automatically.
             * For that, you can run server in debug mode:
                ```
                python manager.py runserver -r
                ```
   * **Directories**
       * All web application projects tend to have at least the following directories:
           * templates - To keep html templates
           * static - This directory has subdirectories - js, img and css to keep static content.
           * uploads - Temporary place to hold uploads from user
