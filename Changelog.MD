# Patten's Personal Finance Tools Changelog

This document will contain all notable changes for Patten's Personal Finance Tools.

The format for this document is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project will adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). 

Dates, where listed, are formatted in accordance to ISO 8601.

## [Unreleased]
- Loan Amorization Calculator
- Loan Payoff Calculator


## [0.1.0] - 2024-12-16

### Added

- Ability to log, and defined the logging defaults.
- Github Actions Integration
    - Automated testing
    - Automated publishing to Github Pages
- Created testing, documentation generation, and command line interface entry points.
- Markdown links to version tags on release headings
- Unreleased section to showcase upcoming features in the next release.

### Changed

- Updated README with Usage information based off of `pyproject.toml` entry points.
- Updated static versioning in `pyproject.toml` and sphinx `conf.py` to be dynamic based on `ppft` version attribute.
- Reformated README with more useful information.

[//]: # (### Removed <- Add this section in when needed)

[unreleased]: https://github.com/TrintenP/ppft/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/TrintenP/ppft/releases/v0.1.0