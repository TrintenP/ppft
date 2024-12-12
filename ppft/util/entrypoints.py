"""
Describes the different entry points for this tool.
"""

import json
import logging.config
import os
import pathlib
import subprocess
import webbrowser


logger = logging.getLogger(__name__)


def setup_logging(
    default_path: str = "./configs/logging.json",
    default_level: int | str = logging.INFO,
    env_key: str = "LOG_CFG",
) -> None:
    """Setup logging configuration, reading in from logging configuration file if possible.

    :param default_path: Location of the logging config JSON, defaults to "./configs/logging.json"
    :type default_path: str, optional
    :param default_level: Level to report for logging, defaults to logging.INFO
    :type default_level: int | str, optional
    :param env_key: Sys. ENV variable containing the path of the config file, defaults to "LOG_CFG"
    :type env_key: str, optional
    """

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    try:
        if os.path.exists(path):
            with open(path, "rt", encoding="utf-8") as fin:
                config = json.load(fin)

                # Verify that the log folder exists
                log_path = pathlib.Path().cwd() / "logs"
                if not log_path.exists():
                    log_path.mkdir(exist_ok=True)

            logging.config.dictConfig(config)
            logger.info("Successfullly loaded in logging configs.")
    except FileNotFoundError:
        # Configuration file not found
        logger.warning(
            "Unable to find specified file, defaulting to basic config."
        )
        logging.basicConfig(level=default_level)
        logger.info("Logging using default configs")


def generate_documentation() -> None:
    """Generates updated documentation from Sphinx."""

    setup_logging()

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

    setup_logging()

    subprocess.run("coverage run -m pytest", check=False)
    subprocess.run("coverage report", check=False)
    subprocess.run("coverage html -d coverage_report", check=False)

    coverage_filepath = pathlib.Path().cwd() / "coverage_report" / "index.html"
    webbrowser.open(coverage_filepath, "1")


def return_true() -> bool:
    """Placeholder for testing scripts to ensure that pts is importable.

    :return: Always returns True.
    :rtype: bool
    """

    return True
