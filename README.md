5 Clicks To Hitler
==================

Mapping the entire 5 Clicks to Hitler game with the Wikipedia API

The goal here is to input a wikipedia page ID or page title and return all link paths to the Adolf Hitler page of length 5 or less.

This is based on the [5 clicks to Hitler](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game) game.

Setting up
----------

    $ virtualenv venv
    $ . venv/bin/activate
    (venv)$ venv/bin/pip install -r requirements.txt
    (venv)$ python clicks.py
    ...work on code...
    (venv)$ deactivate
    $ ...back to normal
