# Rental Management System

## Overview

This Rental Management System is a web application that helps property managers or landlords manage their tenants, flats, units, and rent collection. The system automatically generates monthly invoices and sends SMS notifications to tenants about their rent on the 25th of each month.

---

## Features

### Admin Panel
- Admin login to securely access the system.
- Manage tenants, flats, units, and rent collections.

### Dashboard
- Overview of total tenants, flats, and units.
- Summary of monthly rental collections.
- Quick links to add new tenants, flats, or units.

### Tenant Management
- Add, edit, and delete tenant details.
- View tenant rental history and current status.
- Search and filter tenants by name, unit, or flat.

### Flat/Unit Management
- Add multiple flats and assign them to specific units.
- Assign tenants to flats/units.
- Track the status of each unit (occupied, vacant, etc.).

### Rent Collection
- Record rent payments, including house rent, water bill, gas bill, service charge, and WiFi.
- Automatically generate and view monthly invoices.
- View rent payment history by tenant or unit.

---

## Technology Stack

- **Frontend**: HTML,CSS,JS,Jquery
- **Backend**: Python with Django
- **Database**: MySQL
- **Authentication**: JWT or session-based authentication for admin login

---

## Requirements

- Python 3.9+
- Django 3.0+
- MySQL

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rental-management-system.git
cd rental-management-system
2. Install Dependencies
Create a virtual environment and install the required dependencies:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
3. Database Configuration
Edit the rental_management/settings.py file to configure the database settings:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rental_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
4. Migrate Database
Run the following command to apply migrations and create the necessary database tables:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser
Create an admin user to access the admin panel:

bash
Copy code
python manage.py createsuperuser
6. Run the Development Server
Start the development server:

bash
Copy code
python manage.py runserver
Visit http://localhost:8000 in your browser to access the application.

7. Configure Twilio for SMS Integration
In the settings.py file, add your Twilio credentials:

python
Copy code
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'
Deployment with Docker
1. Build Docker Image
bash
Copy code
docker-compose build
2. Run Docker Container
bash
Copy code
docker-compose up
The app should be running on http://localhost:8000.

Usage
Admin can log in via the /admin/ URL to access the admin panel.
Tenants, flats, and units can be managed via the admin interface.
Rent payments can be tracked, and invoices are automatically generated each month.
SMS reminders are sent to tenants on the 25th of each month.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements.

[Live Demo](https://yamin1.pythonanywhere.com/).


