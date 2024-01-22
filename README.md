# AutoCompany Project

Welcome to the AutoCompany project! This project is aimed at modernizing a company specialized in car parts, enabling them to sell their products online.

## Tech Stack

- Python 3.8 
- Django Framework 4.0.3
- Database ORM 

## Setup Guide for New Developers

### 1. Clone the Repository

```
git clone <repository_url>
cd <project_directory>
```

### 2. Create and Activate a Virtual Environment

```
python3 -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Create a Superuser
```
python manage.py createsuperuser
```

### 6. Run the Development Server
```
python manage.py runserver
```

### 7. Access Django Admin
Visit http://127.0.0.1:8000/admin/ to log in using the superuser credentials.


## Docker Containers

### Build Docker Containers
```
docker-compose build
```

### Apply Migrations
```
docker-compose run web python manage.py migrate
```

### Create Superuser (Optional but recommended for Django Admin access)
```
docker-compose run web python manage.py createsuperuser
```

### Run the Project
```
docker-compose up
```


## API Endpoints
- Products: /api/products/ (As a company, I want all my products in a database, so I can offer them via our new platform to customers)
- Shopping Carts: /api/shopping-carts/ 
- Orders: /api/orders/ 
- Clients: /api/clients/

Additional custom actions for clients:
- Add to Cart: /api/clients/<client_id>/add-to-cart/ (As a client, I want to add a product to my shopping cart, so I can order it at a later stage)
- Remove from Cart: /api/clients/<client_id>/remove-from-cart/ (As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need)
- Place Order: /api/clients/<client_id>/place-order/ (As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car)


Visit http://127.0.0.1:8000/swagger/ in your browser to view the Swagger documentation.~