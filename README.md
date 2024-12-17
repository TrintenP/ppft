# Patten's Personal Finance Tools

PPFT was created as a personal project which will explore how to code a variety of personal finance tools in Python. As well as a learning opportunity in how to package projects.

Initially, this code will only be available via GitHub but hopfully in the future this project will be hosted on PyPI.

- **Documentation**:  https://trintenp.github.io/ppft/
- **Source Code**: https://github.com/TrintenP/ppft
- **Bug Reports**: https://github.com/TrintenP/ppft/issues


## Installation:
- Ensure that Python version installed is 3.12 or better:
    - `python --version`
- Clone GIT repo
    - `git clone https://github.com/TrintenP/ppft.git`
- Change into Cloned repo
    - `cd ppft`
- Create virtual environment
    - `python -m venv .venv`
- Activate virtual environment
    - `.venv\Scripts\activate`
- Install requirements
    - `pip install -r requirements.txt`
- Build the project
    - `python -m build`
- Install the project
    - `pip install -e .`

## Usage
This project will create a set of entry points that can be used in the console. 

`generate-docs`: Will automatically generate, and open, a local copy of documentation.

`ppft-testing`: Will run the entire test suite for ppft, generate a coverage report, and open it.

`run-ppft`: Will run ppft while parsing command line inputs. 

- Arguements:
    - TBA
