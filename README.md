# Add Authentication and SSO to Your Flet App

This repository demonstrates how to integrate Descope authentication and SSO into a Flet application. It is tailored to assist developers who are either building new cross-platform apps with Flet's Python framework or looking to add authentication to existing Flet apps.

## Getting Started

To run this project locally:

1. Follow along with the article to configure Descope and Okta and retrieve all the necessary credentials.

2. Clone this repo, `cd` into the project root folder, create a virtual environment, activate it and install all the dependencies:

    ```bash
    git clone --single-branch -b main https://github.com/kimanikevin254/descope-flet-auth-sso.git

    cd descope-flet-auth-sso

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt
    ```

3. Rename `.env.example` to `.env` and provide the necessary values.

4. Run the apploication using the command `flet run -w --port 8550`.

5. Navigate to "http://localhost:8550" on your browser and check out the application.
