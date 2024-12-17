"""Contains functions that are useful."""

import json
import logging.config
import os
import pathlib

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


def return_true() -> bool:
    """Placeholder for testing scripts to ensure that pts is importable.

    :return: Always returns True.
    :rtype: bool
    """

    return True
