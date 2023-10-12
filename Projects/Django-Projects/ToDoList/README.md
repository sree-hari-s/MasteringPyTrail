# To Do List 
The Todo List project is a simple and effective task management application designed to help you stay organized and productive.

## Features
* Easily add new tasks or to-dos to your list. You can include a title, description, due date, and priority level.
* Securely log in to your account to access and manage your tasks. You can also have multiple users with their own lists and settings.
* Your tasks are stored securely, and changes are synchronized across devices, so you can access your to-dos from anywhere.

## Getting Started

To get started with EduFlow, follow these steps:

1. Install Python 3.x and pip on your system.
2. Clone this repository to your local machine using
```shell
    git clone https://github.com/your_username/ToDoList.git
    cd ToDoList
```
3. Create and activate a virtual environment 
```shell
    python3 -m venv env 
    source env/bin/activate
```
4. Install the dependencies 
```shell
    pip install -r requirements.txt
```

5. Add the environment variables
```shell
    cp .env_sample .env
```

6. Edit the environment variables


7. Run the migrations 
```shell
    python manage.py migrate
```
8. Create a superuser account 
```shell
    python manage.py createsuperuser
```
9. Start the development server 
```shell
    python manage.py runserver
```
10. Navigate to http://localhost:8000 in your web browser to access the application.


## Contributing

We welcome contributions from anyone who is interested in improving EduFlow. To contribute, follow these steps:

- Fork this repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them to your branch.
- Push your changes to your forked repository.
- Submit a pull request to this repository with a detailed description of your changes.
