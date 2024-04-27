# Gas Utility Service App

Django Based Gas Service Application
## Features
**Service requests**: The application would allow customers to submit service requests online. This would include the ability to select the type of service request, provide details about the request, and attach files.

**Request tracking**: The application would allow customers to track the status of their service requests. This would include the ability to see the status of the request, the date and time the request was submitted, and the date and time the request was resolved.

These instructions will guide you through setting up and running the Gas Utility Service APP on your local machine for development and testing purposes.

### Requirements

- Python (3.8 or later)
- Django (3.2 or later)

### Installation

1. **Clone the Repository**

    ```bash
    https://github.com/saishchaskar/gas_utility.git
    ```

2. **Create and Activate a Virtual Environment**

    - For Unix/macOS:
    
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - For Windows:
    
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
        
3. **Migrate the Database**

    ```bash
    python manage.py migrate
    ```
4. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```
    
    Visit `http://127.0.0.1:8000/` in your web browser to view the application.

### Usage

- **Customer Use**: Navigate to `http://127.0.0.1:8000/` to register or login. Once logged in, you can submit new service requests and track existing ones through the dashboard.
- **Admin Use**: Log in to the admin panel at `http://127.0.0.1:8000/admin` using your superuser credentials. Here, you can manage users, view, and resolve service requests.

-  # Outputs

-  ![Screenshot (161)](https://github.com/saishchaskar/gas_utility/assets/102912746/d394c56b-2d21-409a-a676-b6a34c8e1b33)
-  ![Screenshot (162)](https://github.com/saishchaskar/gas_utility/assets/102912746/22f5ea98-21c5-4011-a03b-7a30a058b981)
-  ![Screenshot (163)](https://github.com/saishchaskar/gas_utility/assets/102912746/01328d74-a323-410c-83ca-b5fac808f7fd)
-  ![Screenshot (164)](https://github.com/saishchaskar/gas_utility/assets/102912746/9d206817-dd86-439c-9c9c-f61172890d96)
-  ![Screenshot (165)](https://github.com/saishchaskar/gas_utility/assets/102912746/2374eb3c-c886-4554-b87c-941d13439952)
-  ![Screenshot (166)](https://github.com/saishchaskar/gas_utility/assets/102912746/69d0f5cd-0d96-4cd2-a1e5-01d85e82a3d8)
-  ![Screenshot (167)](https://github.com/saishchaskar/gas_utility/assets/102912746/92f6a73f-a58a-47fc-b6ef-93414dedab0f)
  






