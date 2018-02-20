# exchangeagram
A Exchangeagram built with getting profile info, sharing photos, liking, commenting, and following features.

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/sachinshepherd/Exchangeagram
    ```

*      Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
*      Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    
* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the exchangeagram service on your browser by using
    ```
        http://localhost:8000/insta/
    ```
    