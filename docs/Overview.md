# Overview

This project is a Python-based web application designed to provide an interactive interface for visualizing and
analyzing geographic data. It leverages GIS (Geographic Information System) capabilities to allow users to interact with
maps, perform spatial queries, and carry out geoprocessing tasks.

## What is product/service/concept

The application is built with a modular architecture, with separate components for handling user interface callbacks,
core logic, and page layouts. It also includes a set of utility scripts for common tasks.

The project is containerized using Docker for easy deployment and consistent runtime environment. It also includes
comprehensive documentation to help users understand the API endpoints, entity relationships, and other aspects of the
application.

The application can be customized and extended to suit a variety of use cases in fields such as urban planning,
environmental management, transportation, and more.

## Glossary

A definition list or a glossary:

First Term
: This is the definition of the first term.

Second Term
: This is the definition of the second term.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Structure

- `callbacks/`: Contains callback modal and response Python scripts.
    - `callback_modal.py`: Defines the modal (popup) windows used in the application.
    - `callback_response.py`: Handles the responses to user actions in the application.
- `callbacks_core.py`: Contains the main logic for how the application responds to user actions.
- `Dockerfile`: Defines the environment in which the application runs in a Docker container.
- `docs/`: Contains documentation files for the project.
    - `api-endpoints.md`: Documentation of the API endpoints provided by the application.
    - `entity-relations.md`: Explanation of the relationships between differpip install dash-deckent entities in the
      application.
    - `wiki-python.md`: A wiki for Python-related topics in the project.
    - `wiki-grasshopper.md`: A wiki for Grasshopper-related topics in the project.
- `gis/`: Contains Geographic Information System (GIS) related scripts.
- `main.py`: The main script to run the project.
- `pages/`: Contains layout Python scripts.
    - `layout_default.py`: Defines the default layout for the application.
    - `layout_grid.py`: Defines a grid-based layout for the application.
    - `layout_landing.py`: Defines the layout for the landing page of the application.
    - `layout_modals.py`: Defines the layout for modal windows in the application.
- `README.md`: Provides an overview of the project and instructions for installation, usage, and contribution.
- `requirements.txt`: Lists the Python package dependencies for the project.
- `static/`: Contains static files like CSS, JavaScript, and image files.
- `utils/`: Contains utility scripts that provide various helper functions used throughout the application.

## Documentation

- [API Endpoints](docs/Endpoints)
- [Entity Relations](sql_tests/entity-relations.md)
- [Python Wiki](docs/wiki-python.md)
- [Grasshopper Wiki](docs/wiki-grasshopper.md)

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

