# Carchive®

This application targets car-importing companies. It aims at organizing the owner’s official documents through a management system, which keeps track of all important documents regarding the cars shown in each showroom.

## Table of Contents

1. About the project (#about)
- First application
- Second application
2. Front end
3. Back end
4. Templates of the first application
- Admin login page
- Admin dashboard page
- Add constant items page
- Add showroom page
- Display showroom
- Edit showroom
5. Templates of the second application
- Showroom login page
- Showroom dashboard page
- Change showroom password page
- Add a new car to the showroom page
- Display car details page
- Edit car information page
6. Used technologies
7. Team members
8. Run Localy





# Carchive®

This application targets car-importing companies. It aims at organizing the owner’s official documents through a management system, which keeps track of all important documents regarding the cars shown in each showroom.

## Table of Contents

1. About the project
   - First application
   - Second application
2. Front end
3. Back end
4. Templates of the first application
   - Admin login page
   - Admin dashboard page
   - Add constant items page
   - Add showroom page
   - Display showroom
   - Edit showroom
5. Templates of the second application
   - Showroom login page
   - Showroom dashboard page
   - Change showroom password page
   - Add a new car to the showroom page
   - Display car details page
   - Edit car information page
6. Used technologies
7. Team members
8. Run localy

## About the project
Our project is intended for car company owners to facilitate and organize their car related details and documents. It consists of two applications, the control panel (admin application) and the user application (car company owners).

The first application is only for the administration use, and it contains 6 HTML pages that provides the ability for the admin to add car brands, models, and car's document types. It also allows the admin to add, edit, and delete showrooms for companies owners.

The second application is intended for the car companies owners, where each company will have their own showroom that allows them to change the showroom password that was created by the admin for security. It also provides them with the ability to add cars to their showrooms, edit the car's details whenever there is ubdates. and display all information and documents for each car.

The fron end of the the application is done by using Bootstrap and CSS. It contains 12 HTML pages in total, and the styling of the project is minimal and user-friendly. Moreover, AJAX was used to communicate with the backend, especially with the showroom dashboard live search functionality, and dynamic dependent dropdown select box in adding and editing car information page.

In regards to the back end, it is done by using python language (Django framework). MTV pattern was used to link the Admin model class with the showroom model with one to many relationship, and linking the showroom model with the car model in one to many relationship. Moreover, the linking relationship between the car model, brandModel model, and the document model is one to many relationship. Validations were added for admin login, showroom login, showroom add and edit forms, and car add and edit froms.

## Templates of the first application
- Admin login page: This page is only for the application administrative team.
  you need to initialize a new admin instance by using the pyhton shell:

```
(djangoPythEnv) λ python manage.py shell

from carchive_app.models import *

>>> import bcrypt

>>> hashed_pw=bcrypt.hashpw('QWER1234'.encode(), bcrypt.gensalt()).decode()

>>> Admin.objects.create(first_name='Admin',last_name='Admin',email='Admin@Admin.com',password=hashed_pw)

<Admin: Admin object (1)>
```

![image](https://github.com/RiyadBustami/python_team_project/blob/1962e9596bc5ba9daf8f4030dcaa400d2909bc58/images/first_admin_login.png)
Then you login with the email and password you added to the admins table

![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_login.PNG)

- Admin dashboard page: This page displays the list of all showrooms in the system. It contains linkes for adding car brands and models, along with needed car's document types. It also contains links for adding, editing and deleting showrooms.
 ![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_dashboard.PNG)

- Add constant items page: This page allows the administrator to add new car brands, models, and document types.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_add_items.png)

- Add showroom page: This page contains a form that allows the admin to add a new showroom to the system.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_add_showroom.PNG)

- Display showroom page: It displays all the information regarding the showroom.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_display_showroom.png)

- Edit showroom page: This page contains a form to edit the information of any showroom when needed.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/admin_edit_showroom.png)

## Templates of the second application
- Showroom login page: This page is the login page for the car company owners.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_login.png)

- Showroom dashboard page: It displays a list of all cars in the specific showroom, and links for displaying, editing, and deleting a certain car.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_dashboard.PNG)

- Change showroom password page: This page allows the car company owner to change their account password for security.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_change_password.PNG)

- Add a new car to the showroom page: This page contains a form for adding a new car to the showroom.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_add_car.PNG)

- Display car details page: It displays all car details and documents.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_display_showroom.PNG)

- Edit car information page: This page is used to edit and update all car information and documents.
![image](https://github.com/RiyadBustami/python_team_project/blob/master/images/showroom_edit_car.PNG)


## Used technologies
   * Python 
   * AJAX
   * HTML
   * CSS 
   * Bootstrap

## Project team members:
  1. Riyad Busttami
  2. Majd Sheikh
  3. Maram Naqeeb
  4. Aseel Adel

## How to run the app for the first time: 


