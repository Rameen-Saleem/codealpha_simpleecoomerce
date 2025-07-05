# Simple E-commerce Django Project

A simple e-commerce website built with Django that allows users to browse products, add them to cart, and complete purchases.

## Features

- Product catalog with categories
- Shopping cart functionality
- User authentication and registration
- Order management
- Admin panel for product management
- Responsive design

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd SimpleEcommerce
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

- `ecommerce_project/` - Main Django project settings
- `store/` - Main app containing models, views, and templates
- `media/` - User-uploaded files (product images)
- `staticfiles/` - Static files (CSS, JS, images)

## Models

- **Product**: Contains product information (name, description, price, image, category)
- **Category**: Product categories
- **Order**: Customer orders
- **OrderItem**: Individual items in orders

## Usage

1. Access the admin panel at `http://127.0.0.1:8000/admin/` to add products and categories
2. Browse products on the homepage
3. Add products to cart
4. Complete checkout process

## Technologies Used

- Django 4.x
- SQLite (development)
- HTML/CSS
- Bootstrap (for styling)

