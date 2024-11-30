# Gas Utility Services Application

Django Framework with MYSQL Database with Cloud Run and Cloud SQL deployment.

 **URL of live application**
  ```bash
  https://gas-utility-app-346834722927.asia-south1.run.app/
  ```
**Sample Cerdentials :**
Username : demo  and  Password : Pune@123
## Features
**Service requests**: The application allows customers to submit service requests online. This includes the ability to select the type of service request, provide details about the request, and attach files.

**Request tracking**: The application allows customers to track the status of their service requests. This includes the ability to see the status of the request, the date and time the request was submitted, and the date and time the request was resolved.

**Request Management**: The application allows Customer Support Repenstatives to track service requests. This includes the ability to manage the request as per the customers and also provides a feature to send email as per the request status to customer.

### Structure of the application
```bash
gas_utility/
├── gas_utility/
│   ├── __init__.py
│   ├── settings.py   # Contains the application settings and configurations with database
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── media/            #   stores the  attachment attached to requests.
│       ├── attachments/     
│          ├── f.webp
│          ├── etc
│
├── services/          # directory where actual application logic exists
│   ├── __init__.py
│   ├── admin.py       # Admin Tool code for managing the requests and interface of the admin portal
│   ├── apps.py
│   ├── models.py      # Database Models to store requests, user information, details of the request 
│   ├── urls.py        # Routes of different pages to navigate 
│   ├── views.py       #  logic to interact with frontend views
│   ├── forms.py       # login and signup forms 
│   ├── migrations/         # contains files related to interact with database
│   ├── templates/          # Frontend HTML files 
│         ├── home.html
│         ├── index.html
│         ├── login.html
│         ├── profile_edit.html
│         ├── service_details.html
│         ├── service_requests.html
│         ├── signup.html
│         └── user_profile.html
│         
│
│
└── static/           # files of the static admin page 
│       ├── admin/
│       ├── css/
│       ├── img/
│       ├── js/
│
│
│
└── staticfiles/
│       ├── profile.css
│
└── requirements.txt    # dependencies required for the applications to be installed
│
└── manage.py
│
│
└── Dockerfile         #  For building image and deploying it on the containers 
```

These instructions will guide you through setting up and running the Gas Utility Service APP on your local machine for development and testing purposes.

### Requirements

- Python (3.8 or later)
- Django (3.2 or later)

### Setup

1. **Clone the Repository**

    ```bash
    https://github.com/saishchaskar/gas_utility.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your_project_dir
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv env
    ```

4. **Activate the virtual environment:**

    On Windows:

    ```bash
    env\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source env/bin/activate
    ```

5. **Install the requirements:**

    ```bash
    pip install -r requirements.txt
    ```
6. **Install the mysqlcilent:**

    ```bash
    pip install mysqlclient
    ```    
    
7. **Database Setup: Set your Database information**
  ```bash
  DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'your_db_name',
         'USER': 'your_user_name',    
         'PASSWORD': 'your_password',
         'HOST': 'Your_IP_Address',  # Use '127.0.0.1' if 'localhost' causes issues
         'PORT': 'Port_number',
         'OPTIONS': {
             'init_command': "SET time_zone='+05:30'",  # Set to UTC
         },
     }
 }
 ```
8. **Migrate Database**
   ```bash
   python manage.py makemigrations                                                                               
   python manage.py migrate
   python manage.py runserver
   ```
    Visit `http://127.0.0.1:8000/` in your web browser to view the application.

### Usage

- **Customer Use**: Navigate to `http://127.0.0.1:8000/` to register or login. Once logged in, you can submit new service requests and track existing ones through the dashboard.
- **Admin Use**: Log in to the admin panel at `http://127.0.0.1:8000/admin` using your superuser credentials. Here, you can manage users, view, and resolve service requests.

-  # Outputs

-  ![Screenshot (532)](https://github.com/user-attachments/assets/d7e9025c-7565-4a2d-b389-ac972c7700e5)
-  ![Screenshot (536)](https://github.com/user-attachments/assets/2ec8146e-7e6a-4912-ac86-4cfb286c8abd)
-  ![Screenshot (534)](https://github.com/user-attachments/assets/dafbafe7-992e-4ecb-8b55-8f5770613d1f)
-  ![Screenshot (525)](https://github.com/user-attachments/assets/a8669cfc-d583-49b2-bba3-25d275499623)
-  ![Screenshot (529)](https://github.com/user-attachments/assets/14d8133e-9cdb-4303-9e9a-5c7bc821c3fc)
-  ![Screenshot (528)](https://github.com/user-attachments/assets/1457aa87-4a68-4ab6-bd19-bba85a350c6e)
-  ![Screenshot (527)](https://github.com/user-attachments/assets/c74c82fc-554a-456e-aa5c-1b299129ff05)
-  ![Screenshot (521)](https://github.com/user-attachments/assets/6a746846-de9c-499c-a236-0ecff6bd1372)
-  ![Screenshot (522)](https://github.com/user-attachments/assets/dc67f1d1-290a-4bc9-b09b-1ba6a0b11061)
-  ![Screenshot (526)](https://github.com/user-attachments/assets/d09555dd-3fcd-48b8-bb04-91af384a9b8d)







