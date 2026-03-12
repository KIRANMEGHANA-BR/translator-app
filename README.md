# Global Translator Web Application

A complete Python/Django web application for translating text across multiple languages with user authentication, translation history, favorites, Dark/Light mode, and PDF/TXT exporting capabilities.

## Features
- **Authentication**: Secure Signup, Login, Logout, Profile Management.
- **Translation Core**: Powered by `deep-translator` (Google Translate API fallback) with AJAX async rendering.
- **Dark/Light Mode**: User preference saved via local storage and toggleable dynamically.
- **Dashboards**: Main Translation view, Translation History, Saved Favorites.
- **Tools**: Copy to clipboard, system share, filter favorites.
- **Exporting**: Download translations as `.txt` or high-quality `.pdf` documents using `xhtml2pdf`.

## Local Development Setup

### 1. Prerequisites
- Python 3.10+
- pip (Python package installer)

### 2. Environment Setup
Clone or navigate to the project directory:
```bash
cd ai_projects/translation_app
```

Create and activate a virtual environment:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Initialization
The project uses SQLite by default, which is perfect for minor to medium traffic. Apply the migrations to create the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
To access the Django Admin panel (`/admin/`):
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```
Visit `http://localhost:8000` in your web browser.

---

## Production Deployment
To deploy this application to a production environment (like Heroku, DigitalOcean, or AWS):

**1. Database Migration:** 
For high availability, switch from SQLite to **PostgreSQL**. You will need to install `psycopg2` and update the `DATABASES` configuration in `core/settings.py`.

**2. Static Files:**
Configure a static file storage (like WhiteNoise or AWS S3).
```bash
# Install WhiteNoise
pip install whitenoise
```
Add it to `MIDDLEWARE` in `settings.py` right after SecurityMiddleware. Also, configure `STATIC_ROOT` and run:
```bash
python manage.py collectstatic
```

**3. Web Server:**
Use `gunicorn` to serve the WSGI application instead of the Django development server:
```bash
pip install gunicorn
gunicorn core.wsgi:application
```

**4. Security Configurations:**
Before deploying, make sure to adjust `core/settings.py`:
- `DEBUG = False`
- `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your-ip']`
- Keep `SECRET_KEY` safe and loaded from environment variables (using `python-dotenv`).

Enjoy translating!
