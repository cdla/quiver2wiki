# quiver2wiki


This is a repository converts quiver notebooks into markdown-based wikis.


## Overview

I have started keeping a personal wiki, and think that using the Quiver app will make that an easier process to organize.

[Quiver](http://happenapps.com/#quiver), made by [happenapps](http://happenapps.com), is known as a programmer's notebook, due to the organizational structure of the notes and the ability to save and organize code snippets.

This is currently a work in progress.

## Installation

1. Download or clone the repository

```bash
git clone git@github.com:cdla/quiver2wiki.git
```

2. cd into the directory and run the setup.

```bash
cd quiver2wiki;
python setup.py
```

You're good to go!

## Usage

```bash
# In order to export your quiver library into markdown files
quiver2wiki -export /quiver/library/location

# Hosting a quiver library
quiver2wiki -host /quiver/library/location

```

## Notes

By default, Quiver saves your library to a location within Application Support. It is recommended that you change that location to somewhere that is backed up and secure.

To do this, open up the settings menu within the quiver app. go to the sync tab, and choose another location on your computer


## TODO
- [x] initialize project
- [ ] add ability to convert notebooks to markdown in batch
- [ ] add ability to ignore private notebooks
- [ ] add ability to locally host notebooks through mkdocs or similar platform
- [ ] add ability to work with nested notebooks
