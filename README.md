# Tradewinds

This is a an ambitious web app which aims to serve all the use cases in a small medium enterprise.


## Setup Guide:
  * You should have these installed:  **python 2.7+** and **pip**
  * **Tox Installation** (try with sudo if there is a permission error):
                ```
                pip install tox
                ```
  * **Project setup**
                ```
                source setup.sh
                ```
    * Following commands will be available after setup:


    | Command    | Description                            |
    |------------|----------------------------------------|
    | run        | Executes python manage.py runserver    |
    | doc        | Opens documentation in a browser       |
    | dspace     | cd into this directory from anywhere   |
    | activate   | Activates the virtual environment      |
    | deactivate | Deactivates the virtual environment    |

      Above commands can be run from any directory

  * **Starting the server**
                ```
                python manage.py runserver
                ```
  * **Dependencies:**
    * Python dependencies are specified in requirements.txt
    * Whenever a new package is added to requirements.txt, please add description/need for it here.
       * gunicorn -  Runs multiple instances of our Django server (for scalability)
       * Django - The 'web-framework'
       * Jinja2  (Templating engine)
       * requests ( HTTP library)
       * sphinx (Documentation tool)
       * sphinx_rtd_theme (Theme for sphinx)


## Documentation
  * Documentation is rebuilt on readthedocs.org whenever a commit is pushed to this repository.
  * You need to create an account on readthedocs.org and add service to your github account.


## Development Guide:

  * **Database**
    * We will be using sqlite for now. Plan is to migrate to PostgreSql when our datamodel design becomes stable.

  * **Routes**
    * /admin - This is the admin panel to manage this application's technicalities and view what data we store.
                This can be accesses at http://localhost:port/admin. Credentials are admin/password.

  * **Directories**
      * All web application projects tend to have at least the following directories:
          * templates - To keep html templates
          * static - This directory has subdirectories - js, img and css to keep static content.
          * uploads - Temporary place to hold uploads from user
