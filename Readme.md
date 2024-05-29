<h1 align="center"> :fire: Firewall Rule Risk Calculator </h1>

<i><span style="color: orange;">Firewall</span></i> Rule Risk Calculator is a simple web application built with Flask to help you calculate the risk associated with different firewall rules. The application provides a user-friendly interface to input various parameters and receive a risk assessment along with recommendations.


## Features

- Calculate firewall rule risk based on multiple parameters
- Provides risk levels (Low, Medium, High, Critical)
- Offers recommendations based on the risk level (To be implemented)
- Expandable documentation for each parameter

## Table of Contents
- [App look](#app-look)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## App look 
![alt text](<app_look.png>)

## Installation

To get started with the Firewall Rules Risk Calculator, follow these steps:

### Prerequisites

- Python 3.7+
- Flask

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/<username>/firewall-risk-calculator.git
   cd firewall-risk-calculator
2. Create and activate a virtual environment:
    ``` 
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the dependencies:
    ``` 
    pip install -r requirements.txt
4. Run the Flask application:
    ``` 
    python3 ./app.py
5. Open your browser and navigate to: "http://localhost:8989'

### Usage
1. Open the web application.
2. Fill in the parameters for the firewall rule.
3. Click the "Calculate Total" button.
4. View the risk assessment and recommendations.

### Docker
To run the application using Docker, follow these steps:
1. Build the docker image:
    ``` 
    docker build -t flask-app .
2. Run the docker container:
    ```
    docker run -p 8989:8989 flask-app
3. Open your browser and navigate to: "http://localhost:8989'

### Documentation

For detailed information about each parameter and why it's important for calculating the risk of firewall rules, visit the http://localhost:8989/documentation page.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

### License
This project is licensed under the MIT License.