## GROUP 2 PROJECT ##

## Real Estate CLI ##
Welcome to the Real Estate CLI project! This command-line interface (CLI) is designed to help a user to search for any listed property,see available listings all from the cli , providing a seamless and efficient way to access real estate information. This README will guide you through the setup, features, and best practices employed in this project.

## Table of Contents ##
*Getting Started
*Configuration and Dependencies
*SQLAlchemy Schema Design
*CLI Best Practices
*DSA Execution
*Contributing
*License

## Getting Started ##
To get started with the Real Estate CLI, follow these steps:

**1.Clone the repository to your local machine.**

bash
Copy code
git clone https://github.com/your-username/real-estate-cli.git
cd real-estate-cli

**2.Install dependencies using Pipenv.**

bash
Copy code
pipenv install

**3.Activate the virtual environment.**

bash
Copy code
pipenv shell

**4.Run the CLI script.**

bash
Copy code
python cli.py

Now you're ready to explore and utilize the Real Estate CLI!

## Configuration and Dependencies ##
**Pipenv Environment**
The project uses Pipenv to manage dependencies. The Pipfile includes all necessary dependencies, and you can install them with the following command:

bash
Copy code
pipenv install

Make sure to activate the virtual environment before running the CLI:

bash
Copy code
pipenv shell

## External Libraries ##
The project makes use of external libraries, such as SQLAlchemy for database management and Click for CLI-related tasks. These libraries enhance the functionality and maintainability of the code.

## SQLAlchemy Schema Design ##
The Real Estate CLI utilizes SQLAlchemy ORM to create and manage a database schema with three or more related tables. Alembic is employed to handle database migrations, ensuring proper organization and version control.

## CLI Best Practices ##
The CLI follows best practices to enhance user experience:

Separation of scripted elements from object-oriented code.
Validation of user input to ensure data integrity.
Detailed prompts and messages to guide users throughout the execution.
Utilization of external libraries (e.g., Click) to minimize project-specific code.

## DSA Execution ##
The Real Estate CLI incorporates data structures such as lists, tuples, and dictionaries. Additionally, an algorithm from the Data Structures and Algorithms module is applied in an appropriate context within the CLI.

## Owners ##
~ Guyo Halake
~ Craig Otieno
~ Ivy Kibe
~ Dennis Kimani
~ Claire Muiru


## Contributing ##
If you would like to contribute to the Real Estate CLI project, please follow the guidelines in CONTRIBUTING.md. We welcome your input and ideas!

## License ##
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to use, modify, and distribute the code according to the terms of the license.

Thank you for choosing the Real Estate CLI. Happy exploring!




