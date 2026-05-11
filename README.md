#  Calorie Counter - Django Web Application

A full-featured web application for tracking daily calorie intake. Built with Django, PostgreSQL, and styled with Tailwind CSS.

**Live Demo:** [https://calorie-counter-app.onrender.com](https://calorie-counter-app.onrender.com) *(Update with your actual deployment URL)*

##  Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local Development Setup](#local-development-setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [Database Management](#database-management)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

##  Features

### Core Functionality
-  **Add Food Items** - Easily add food items with calorie counts
-  **View Daily List** - See all food items consumed today
-  **Delete Items** - Remove incorrect entries
-  **Daily Total** - Automatic calculation of daily calorie intake
-  **Reset Count** - Clear today's entries to start fresh
-  **Date History** - View and manage past entries
-  **Weekly Chart** - Visualize the last 7 days of intake

### User Interface
-  **Responsive Design** - Works on desktop, tablet, and mobile devices
-  **Tailwind CSS** - Modern, clean styling
-  **Charts.js Integration** - Visual representation of daily data
-  **Real-time Updates** - Instant feedback on actions

### Technical Features
-  **Input Validation** - Server-side and client-side validation
-  **Performance Optimized** - Database indexing and query optimization
-  **Production Ready** - Configured for deployment to Render
-  **Well Documented** - Comprehensive comments and docstrings
-  **Security Best Practices** - CSRF protection, XSS prevention, secure headers

##  Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Backend | Django | 3.2.15 |
| Database | PostgreSQL | 12+ |
| Frontend | HTML5, Tailwind CSS | Latest |
| Server | Gunicorn | 20.1.0 |
| Python | Python | 3.10+ |
| Version Control | Git | Latest |

## Project Structure

```
calorie_counter_project/
├── calorie_counter_project/        # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Project URL routing
│   ├── wsgi.py                     # WSGI application
│   └── asgi.py                     # ASGI application
├── calorie_tracker/                # Main Django app
│   ├── migrations/                 # Database migrations
│   ├── templates/                  # HTML templates
│   │   ├── base.html              # Base template
│   │   ├── index.html             # Home page
│   │   └── history.html           # History page
│   ├── static/                     # Static files (CSS, JS)
│   ├── models.py                   # Database models
│   ├── views.py                    # View logic
│   ├── forms.py                    # Form classes
│   ├── urls.py                     # App URL routing
│   └── admin.py                    # Admin interface
├── manage.py                        # Django CLI
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore rules
├── Procfile                         # Render deployment config
├── runtime.txt                      # Python version
└── README.md                        # This file
```

##  Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- Git
- pip (Python package installer)
- Virtual environment (recommended: venv or virtualenv)

##  Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/calorie-counter.git
cd calorie-counter
```

### 2. Create a Virtual Environment

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and update with your settings:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Configuration
DB_NAME=calorie_counter
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create PostgreSQL Database

```bash
# Create database
createdb calorie_counter

# If you need to create PostgreSQL user
createuser postgres  # or use existing user
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

##  Configuration

### Django Settings

Key settings in `settings.py`:

- **DEBUG**: Set to `False` in production
- **SECRET_KEY**: Generate a strong secret key for production
- **ALLOWED_HOSTS**: List of allowed host names
- **DATABASES**: Database connection configuration
- **INSTALLED_APPS**: List of installed Django apps
- **MIDDLEWARE**: Middleware classes for request/response processing

### Database Configuration

The application supports:

- **Development**: PostgreSQL (configurable in `.env`)
- **Production**: PostgreSQL via `DATABASE_URL` environment variable

### Static Files

- All static files are served via WhiteNoise in production
- CSS and JavaScript are included via CDN (Tailwind CSS, Chart.js)
- Custom CSS is in `static/css/style.css`

## Running the Application

### Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Access Admin Panel

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials.

##  Usage Guide

### Adding Food Items

1. Enter the food item name (e.g., "Apple", "Chicken Breast")
2. Enter the calorie count
3. Select the date (defaults to today)
4. Click "Add Food Item"

### Viewing Items

- **Today's List**: Main page shows all items added today
- **Weekly Chart**: Visual representation of the last 7 days
- **History**: Navigate to History to view past entries

### Removing Items

1. Find the item in the list
2. Click the trash icon next to the item
3. Confirm deletion

### Resetting Daily Count

1. Click "Reset Today's Count" button
2. Confirm the reset action
3. All items for today will be removed

##  Database Management

### Create Backup

```bash
pg_dump calorie_counter > backup.sql
```

### Restore from Backup

```bash
psql calorie_counter < backup.sql
```

### Migrations

Create migrations after model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

View migration history:

```bash
python manage.py showmigrations
```

## Deployment

### Deploy to Render

Render is recommended for easy Django deployment.

#### Prerequisites

1. GitHub repository with your code
2. Render account (free tier available)
3. PostgreSQL database (Render provides this)

#### Step-by-Step Deployment

1. **Create PostgreSQL Database on Render**
   - Sign up at https://render.com
   - Click "New +" → "PostgreSQL"
   - Follow the setup wizard
   - Note the External Database URL

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Select your GitHub repository
   - Configure settings:
     - **Name**: calorie-counter
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
     - **Start Command**: `gunicorn calorie_counter_project.wsgi`

3. **Set Environment Variables**
   - In Render dashboard, go to your web service
   - Click "Environment"
   - Add variables:
     ```
     DEBUG=False
     SECRET_KEY=<generate-a-new-secret-key>
     DATABASE_URL=<paste-postgresql-external-url>
     ALLOWED_HOSTS=your-app.onrender.com
     ```

4. **Generate Secret Key**
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

5. **Deploy**
   - Push code to GitHub
   - Render will automatically deploy

#### Other Deployment Options

**Heroku** (Similar process, requires Heroku CLI)
**AWS** (EC2 with RDS database)
**DigitalOcean** (App Platform or Droplet)
**PythonAnywhere** (Beginner-friendly)

### Production Checklist

- [ ] DEBUG set to False
- [ ] SECRET_KEY changed to new secure value
- [ ] ALLOWED_HOSTS configured
- [ ] Database migrations run
- [ ] Static files collected
- [ ] HTTPS enabled
- [ ] Environment variables set
- [ ] Email backend configured (optional)
- [ ] Backup strategy in place
- [ ] Monitoring setup

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'django'"**
- Solution: Ensure virtual environment is activated and dependencies are installed
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**Issue: "psycopg2.OperationalError: could not connect to server"**
- Solution: Check PostgreSQL is running and connection settings are correct
  ```bash
  psql -U postgres -h localhost
  ```

**Issue: Static files not loading**
- Solution: Run collectstatic
  ```bash
  python manage.py collectstatic --noinput
  ```

**Issue: Migration conflicts**
- Solution: Resolve migration conflicts
  ```bash
  python manage.py migrate --fake-initial
  ```

**Issue: Render deployment fails**
- Solutions:
  - Check build logs in Render dashboard
  - Verify DATABASE_URL is set correctly
  - Ensure secret key is strong and set
  - Check ALLOWED_HOSTS includes your domain

### Debug Mode

Enable detailed error pages (development only):

```python
# settings.py
DEBUG = True  # Only in development!
```

##  Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Render Deployment Guide](https://render.com/docs)
- [Chart.js Documentation](https://www.chartjs.org/docs)

##  Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  Code Standards

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for all functions
- Keep templates DRY (Don't Repeat Yourself)

##  License

This project is licensed under the MIT License - see LICENSE file for details.
