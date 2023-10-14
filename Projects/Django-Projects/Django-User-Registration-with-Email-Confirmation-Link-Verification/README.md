# Django User Registration with Email Confirmation Link Verification

This Django project allows users to register with their email addresses and verifies their email through a confirmation link sent via email.

## Features

- User registration with username, first name, last name, email, and password.
- Unique username and email validation.
- Password matching validation.
- Email confirmation link sent to the user's registered email address.
- Account activation upon successful email confirmation.
- User login with username and password.
- User logout.
## Result
# Django User Registration with Email Confirmation Link Verification

https://github.com/sobit-nep/Django-User-Registration-with-Email-Confirmation-Link-Verification/assets/65544518/5fa7f917-d4cb-41b6-bfa0-f0500cfadfee



## Prerequisites

Make sure you have the following installed:

- Python (version 3.7 or higher)
- Django (version 3.0 or higher)


## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/sobit-nep/MasteringPyTrail.git
   ```

2. Go to project directory and create a virtual environment and activate it:
   ```
   cd MasteringPyTrail\Projects\Django-Projects\Django-User-Registration-with-Email-Confirmation-Link-Verification
   pip install virtualenv
   virtualenv venv
   venv\scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application in your web browser at `http://localhost:8000/`.

## Configuration

1. Set up email settings in `settings.py`:

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_email_host'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email_address'
EMAIL_HOST_PASSWORD = 'your_email_password' #password generated from security page on manage account section of your email account(search for "App Password")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'your_default_from_email_address'
```

2. Configure the email templates for email confirmation and activation in the templates directory.

## Usage
1. Register a new user by providing a username, first name, last name, email, and password.
2. After successful registration, an email with a confirmation link will be sent to the provided email address.
3. Click on the confirmation link in the email to activate the account.
4. Login with the registered username and password.
5. Logout from the application.


## Acknowledgements
1. This project is based on Django, a high-level Python web framework.
2. It utilizes Django's built-in user authentication and email sending capabilities.
3. The project uses Bootstrap for styling the frontend forms and pages.
4. Special thanks to the Django community for providing valuable resources and documentation


Feel free to customize and expand upon this `README.md` file according to your project's specific requirements and structure.

Remember to include any additional installation steps, project structure information, or important details that would be helpful for users who want to run or contribute to your project.

Make sure to update the prerequisites, configuration instructions, and acknowledgments section based on the libraries, frameworks, and resources you have used in your project.

Good luck with your Django user registration project!


