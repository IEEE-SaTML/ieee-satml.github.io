# SaTML website

This website is built using Pelican, a static site generator using Python and Markdown.

## Getting Started

To set things up locally, first create a virtual environment and install the required dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "pelican[markdown]"
```

## Running the Development Server

You can preview the site locally with automatic reloading by running:
```
make devserver
```

Once it's running, head over to http://localhost:8000 to preview the site.

## Structure

Here's a quick overview of the project's structure:

- `pelicanconf.py`: Main configuration file
- `data/`: Structured data (e.g., organizing committee)
- `content/`: The core site content, written in Markdown

The site uses a custom SaTML theme based on the Bulma CSS framework. The files are located under `theme/templates/`. 

For more details, see the [Bulma documentation](https://bulma.io) and [Pelican documentation](https://docs.getpelican.com/en/latest/).

