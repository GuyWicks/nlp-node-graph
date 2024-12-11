# nlp-node-graph

Some initial proof-of-concepts using NLP to generate graph networks and visualise them.

Packages used:
- [FastAPI](https://fastapi.tiangolo.com/)
- [jinja](https://jinja.palletsprojects.com/en/stable/templates/)
- [spacy](https://spacy.io/api)
- [networkx](https://networkx.org/documentation/stable/)
- [pyvis](https://pyvis.readthedocs.io/en/latest/documentation.html)

## Installation

Preequisites: 
- github credentials etc...
- Python 3.12.x (recommend use `pyenv`)
- GNU `make`, `git`
- `pip install virtualenv`
- [Visual Studio Code](https://code.visualstudio.com/)

Then you can attempt this:
``` bash
> git clone git@github.com:GuyWicks/nlp-node-graph.git
> make install
> make spacy_install_model
```

## How to use

`make start` and point your browser to http://127.0.0.1:8011

- [Nodes](http://127.0.0.1:8011/) tries to visualise a node graph based on 'rules' in `data\rules\*.txt`. 
- [NLP](http://127.0.0.1:8011/nlp) allows you to test and visualise NLP tokenisation.  See the _spacy_ documentation for details
- [Docs](http://127.0.0.1:8011/docs) provides access to the FastAPI api that will be built up to support the modelling

## Rules

Rules are simple axioms that can be combined to create a larger 'context graph'. For example:

```
"data\rules\flowers.txt"

Roses are red
Violets are blue
Roses and Violets are Flowers
```

...should yield a graph like:

```
(red) <--are-- [rose] ---type of---.
                                    >---> ||flower||
(blue) <--are-- [violet] --type of-'
```

Where 'red' is a 'colour' property (attribute) of a 'flower', and a rose is an instance of a flower.

## How does this work

It doesn't!  Lots of working out to do!

See [TODO](TODO.md) for 