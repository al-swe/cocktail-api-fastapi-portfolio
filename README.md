# Cocktail API

The Cocktail API is a backend service designed to support a cocktail recipe website. This API provides several endpoints that allow users to retrieve cocktail recipes, search by various criteria, and explore different types of alcoholic beverages.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Features

This API includes the following endpoints:

- **/all-cocktails**: Retrieve a list of all available cocktails.
- **/cocktail/{id}**: Fetch details of a specific cocktail by its ID.
- **/random-cocktail**: Get a randomly selected cocktail.
- **/alcohol-types**: List all available types of alcohol used in the cocktails.
- **/cocktail-by-tag**: Find cocktails based on specific tags.
- **/docs**: Access the API documentation via Swagger.

## Technologies Used

- **Python**
- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Vercel**: Used for deployment of the API.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/al-swe/cocktail-api-fastapi.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd cocktail-api-fastapi
    ```

3. **Set up a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application locally, use the following command in your terminal:

```bash
uvicorn main:app --reload
