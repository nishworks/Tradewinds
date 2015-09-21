Mandi - Managing grains

This is a an ambitious web app which aims to serve all the use cases in a grain market.

Development Guide:

   * You should have following installed:
     * python 2.7
     * pip
   * Setting up Project:
     * Tox Installation (try with sudo if there is a permission error):
                ```
                pip install tox
                ```
     * Once you are in the project root directory and you have tox installed, execute
                ```
                tox
                ```
     * This will create a virtual environment under '.tox' directory and will install all the python packages in it
         specified by requirement.txt.
     * To activate virtual environment- In the project root, execute
                ```
                source activate
                ```
     * To start the server.
                ```
                python manage.py runserver
                ```
     * Dependencies (Specified in requirement.txt)
       Whenever a new package is added to requirements.txt, please add description/need for it here.
       * gunicorn -  Runs multiple instances of our Flask server (for scalability)
       * Flask - (The micro web-framework)
       * Flask-Script (Required by manage.py for command CLI)
       * Flask-SQLAlchemy  (Useful utilities over SQL-Alchemy for use in Flask)
       * SQLAlchemy==1.0  (Object-Relational-Mapper, https://en.wikipedia.org/wiki/Object-relational_mapping)
       * ipython (Nice alternative to official python shell)
       * Jinja2  (Templating engine)
       * requests ( HTTP library)
     * Web App:
       * Work in progress...
     * Data-Store:
       * We are going to use sqlite for now. (sqlite3 is included in python standard library).
       * It is a file based database.
