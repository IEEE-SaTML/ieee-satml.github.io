# SaTML Website

Welcome! This is the source for the SaTML conference website, built with [Pelican](https://docs.getpelican.com/en/latest/) (a static site generator) and [Bulma](https://bulma.io) (a CSS framework).


## Getting Started

To set things up locally, create a virtual environment and install the required dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
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
- `theme/templates/`: The template files

## Adding a New Edition

Each edition of the conference is organized in an (ideally) self-contained repository under the IEEE SaTML GitHub organization. The domain **satml.org** is linked to this organization, which allows to serve any of its repositories via GitHub Pages under https://satml.org/<repository-name>.

The **current edition** is served directly under `https://satml.org`, which is tied to the special repository **ieee-satml.github.io**.

To add a new edition:

1. **Archive the current site**:
   - Duplicate the content of the main repository `ieee-satml.github.io` into a new repository named after the year (e.g., `2026`).
   - This repository should be deployed at `https://satml.org/2026`.
   - In `pelicanconf.py`, update the `SITEURL` to reflect this new location.
   - Fix any internal links that may broke due to the move.

2. **Create the new main site** in `ieee-satml.github.io`:
   - This repository will serve the new edition directly under `https://satml.org`.
   - It should be completely independent of the previous one.
   - Include links pointing to past editions (e.g., 2023, 2024, etc.).

### Misc

- The files `gitlab-ci.yml` and `pelicandevconf.py` are used for the development server at TU Berlin. They are not required for deployment on GitHub and may be removed in a future cleanup.
- The deployment workflow for GitHub Pages is defined in `.github/workflows/deploy.yml`.