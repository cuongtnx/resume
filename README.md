# CUONG TRAN RESUME

The page is manually customized for desktop, mobile and printing.

## Technology

- Flask
- Freeze
- Sass

### Front-end

- HTML & CSS (SASS)

### Back-end

The page is built using the `Flask` framework, using `Flask-frozen` to convert the page to static.

## Editing Guide

- Create & activate virtual environment 

`virtualenv env`

`source env/bin/activate`

- Install requirements

`pip install -r requirements.txt`

- Runsever 

`python run.py`

- Run Sass watcher

`sass --watch --style compressed resume/static/scss:custom.scss:resume/static/css/custom.css`

- After editing, run `freeze.py` to convert site to static.
