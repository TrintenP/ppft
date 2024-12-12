"""
Contains functions that will handle various forms of parsing.
"""

import argparse
import sys
import logging

logger = logging.getLogger(__name__)


def parse_input(arg_list: list | None = None) -> argparse.Namespace:
    """Parses inputs from command line, and creates a namespace for them.

    :param arg_list: CMD-styled inputs of strings, defaults to sys.argv[1:]
    :type arg_list: list

    :return: Namespace that contains all parsed inputs for the given arguements
    :rtype: argparse.Namespace
    """
    if arg_list is None:
        arg_list = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="Parse inputs from Command Line."
    )

    args = parser.parse_args(arg_list)

    logger.info("Args read in from CLI are: %s", args)

    return args
