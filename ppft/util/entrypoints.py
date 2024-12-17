"""
Describes the different entry points for this tool.
"""

import argparse
import logging
import os
import pathlib
import subprocess
import webbrowser

from ppft.util import general
from ppft.util import parsing


logger = logging.getLogger(__name__)


def generate_documentation() -> None:
    """Generates updated documentation from Sphinx."""

    general.setup_logging()

    orig_cwd = pathlib.Path().cwd()

    # Ensure that we are in the docs folder for Sphinx
    docs_folder = orig_cwd / "docs"
    os.chdir(docs_folder)

    # Automatically creates .rst files for Sphinx
    gen_process = subprocess.run(
        "sphinx-apidoc -o ./source ../ppft",
        check=False,
        stdout=subprocess.DEVNULL,
    )

    if gen_process.returncode != 0:
        logger.warning(
            "Something went wrong with generating API docs, returned value of %d",
            gen_process.returncode,
        )
        return

    make_location = pathlib.Path("./make.bat").resolve()

    logger.info("Sphinx-apidoc successful, building documentation now.")

    # Remove any previous documents just in case
    subprocess.run(f"{make_location} clean", check=False)

    # Use clean in-case of previous errors
    make_process = subprocess.run(
        f"{make_location} html",
        check=False,
        stdout=subprocess.DEVNULL,
    )

    if make_process.returncode != 0:
        logger.warning(
            "Something went wrong with making docs, returned value of %d",
            make_process.returncode,
        )
        return

    doc_file_str = str(pathlib.Path("./build/html/index.html").resolve())
    logger.info("Successfully create documentation at: %s", doc_file_str)
    webbrowser.open(doc_file_str)

    os.chdir(orig_cwd)


def run_testing() -> None:
    """Runs coverage for test suite for patten's tool suite."""

    general.setup_logging()

    subprocess.run("coverage run -m pytest", check=False)
    subprocess.run("coverage report", check=False)
    subprocess.run("coverage html -d coverage_report", check=False)

    coverage_filepath = pathlib.Path().cwd() / "coverage_report" / "index.html"
    webbrowser.open(coverage_filepath, "1")


def run_cli(arg_list: list | None = None) -> None:
    """Runs the tool in general command line mode. Takes input from the command line interface.

    :param arg_list: CMD-styled inputs of strings, defaults to sys.argv[1:]
    :type arg_list: list | None, optional
    """

    general.setup_logging()

    if arg_list is None:
        args = parsing.parse_input()
    else:
        args = parsing.parse_input(arg_list)

    logger.info("Args returns to entrypoint location")  # Temp statement
