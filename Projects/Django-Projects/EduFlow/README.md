# EduFlow - School Management Website

EduFlow is a web-based school management system designed to help schools manage their administrative tasks more efficiently. It provides a centralized platform for managing student data, courses, timetables, attendance, grades, fees, library, and alumni information.

## Features

* Student information management: Manage and update student profiles, including personal information, academic progress, grades, attendance, and disciplinary records.
* Teacher information management: Manage teacher profiles, including personal information, teaching experience, and qualifications.
* Course management: Create and manage courses, assign teachers and students to them.
* Gradebook management: Manage and record student grades, create gradebooks and input grades electronically.
* Fee management: Manage student fees, generate invoices, accept online payments, and track payment history.
* Library management: Manage the school library, check out and return books, track inventory, and place holds.

## ER Diagram

<img src="./ER_Map.png" />

## Getting Started

To get started with EduFlow, follow these steps:

1. Install Python 3.x and pip on your system.
2. Clone this repository to your local machine using

    ```shell
        git clone https://github.com/your_username/EduFlow.git
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

10. Navigate to [http://localhost:8000](http://localhost:8000) in your web browser to access the application.

## Contributing

We welcome contributions from anyone who is interested in improving EduFlow. To contribute, follow these steps:

* Fork this repository.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them to your branch.
* Push your changes to your forked repository.
* Submit a pull request to this repository with a detailed description of your changes.

## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](LICENSE) file for details.
