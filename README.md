# SaTML Website

Welcome! This is the source for the SaTML conference website, built with [Pelican](https://docs.getpelican.com/en/latest/) (a static site generator) and [Bulma](https://bulma.io) (a CSS framework).


## Getting Started

To set things up locally, create a virtual environment and install the required dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "pelican[markdown]"
```

## Running the Development Server

To preview the site locally with automatic reloading, run:
```
make devserver
```

Once it's running, head over to http://localhost:8000 to preview the site.

## Structure

- `pelicanconf.py`: Main configuration file
- `data/`: Structured data (e.g., organizing committee)
- `content/`: The core site content
- `theme/templates/`: The custom SaTML theme