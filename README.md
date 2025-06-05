# SaTML website

This website is built using Pelican, a static site generator using Python and Markdown.

## Getting Started

To get started, create a virtual environment and install the required packages:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install "pelican[markdown]"
```

## Running the Development Server

To start the local development server with automatic reloading:
```
make devserver
```

Visit http://localhost:8000 to preview the site.