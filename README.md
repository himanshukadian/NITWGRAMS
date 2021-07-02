# NITWGRAMS
This is a "NITW Grievance Rendering and Management System" which gives students the ability to register their grievances and get solution to them.

The backend is completely build on Django and frontend using html, css, bootrap and javascript and used  tensorflow for NLP.
### Features
* Different roles defined i.e Students, Admin, Carpenter, Mess, Chief Warder, Electrician and Accounts.
* Login/Registration for students
* Student can Register their grivance to any of the department.
* They can chat to each other.
* Social Auth is also there for student login.
* Here Students only need to enter the subject for thier grievance and it will automatically send it to concerned department.

## Project Setup
1. Clone this repository: `https://github.com/himanshukadian/NITWGRAMS.git`.
2. Change the current directory to folder: `cd ./NITWGRAMS`.
3. Create a virutal environment and install all backend dependencies with pip: `pip install -r requirements.txt`.
4. Start the virtual environment: `env\Script\activate`.
5. Run `python manage.py makemigrations`.
6. Run `python manage.py migrate`.
7. Create a superuser: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`.

## Tech Stack Used
1. Django
2. HTML, CSS  and JavaScript
3. Tensorflow for NLP
