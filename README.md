
Student Management System
==========================

Description:
--------------------
1. The Student Management System is a comprehensive web-based application serving students, trainers, and administrators in educational institutions.

2. It offers customized functionalities for each user role, ensuring their individual needs are met.

- Administrators can efficiently manage student, trainer, and course information across departments such as IT, Civil, and Mechanical. 
  They can also utilize the integrated todo app to organize tasks and schedules effectively.

- Trainers have access to a personalized dashboard for viewing and overseeing their assigned students.

- Students can register themselves within the system and enroll in courses offered by their respective departments. 
  After enrollment, students can log in to access their personal data, and even upgrade to the next level course as per their academic requirements.

Installation:
--------------------

1. run this commands on terminal 
- py manage.py makemigrations
- py manage.py migrate


2. create superuser 
- python manage.py createsuperuser (to create admin)


3. Run server : 
- For windows : py manage.py runserver
- For Linux/Mac : python manage.py runserver


4. Open Browser and in url add - .../admin
- login using username & password (created  while creating superuser)


5. This username & password for admin login
- Now Click on "trainers" here we have to create username & passwords for trainers of each department


6. Run: py manage.py runserver
- Now, you will see different options like "Manage Course", "Add Trainer", "Enquiries", and "Todo App".
- Manage Course: You can Add,Modify or delete the courses for various departments
- Add Trainer: Able  to add new trainer with details and can also modify or delete
- Enquiries: All enquiries, including today's enquiries, can be viewed and downloaded in CSV format.

--------------------

### Home Page
![studentmanagement](https://github.com/sejalkoli/Student-Management-System/assets/116626091/b1399079-646a-4be3-91c4-c07d83bbbc26)

--------------------
### Admin Page

![adminpg](https://github.com/sejalkoli/Student-Management-System/assets/116626091/04b717ac-996c-436d-8739-2cdbbc4d0ea4)



