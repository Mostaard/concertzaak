# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Concertzaak is a Django 4.2 web application built with Wagtail CMS 5.2 for managing concert information, blog posts, and rehearsal guides. The site is localized for Dutch-speaking Belgian audience (nl-BE).

**Stack:**
- Django 5.0 LTS (supports PostgreSQL 12+)
- Wagtail 6.4
- PostgreSQL (psycopg2)
- wagtailmenus for navigation

**Dependency Management:**
- Uses `pip-tools` for reproducible builds
- `requirements.in` - direct dependencies (edit this)
- `requirements.txt` - locked dependencies (auto-generated)

## Environment Setup

**Virtual environment is located in `.venv` directory.** Activate before running commands:
```bash
source .venv/bin/activate
```

**Database:** PostgreSQL with default credentials configured in `concertzaak/settings/local.py`:
- Database: `concertzaak`
- User: `admin`
- Password: `admin`
- Host: `127.0.0.1:5432`

## Common Commands

### Development Server
```bash
python manage.py runserver
```

### Database Management
```bash
# Apply migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations

# Create superuser for Wagtail admin
python manage.py createsuperuser
```

### Static Files
```bash
# Collect static files (required after CSS/JS changes)
python manage.py collectstatic --noinput
```

### Dependency Management
```bash
# Add a new dependency: edit requirements.in, then:
pip-compile requirements.in
pip-sync requirements.txt

# Upgrade all dependencies to latest compatible versions:
pip-compile --upgrade requirements.in
pip-sync requirements.txt
```

### Wagtail Admin
Access at: `http://localhost:8000/admin/`

## Architecture

### Settings Structure
Settings are split across multiple files in `concertzaak/settings/`:
- `base.py` - Shared configuration
- `dev.py` - Development settings (uses `dev` as default via `manage.py`)
- `local.py` - Local overrides (database, email, secrets) - **NOT in git**
- `production.py` - Production settings

### App Structure
All Django apps are located in `concertzaak/apps/`:

**`core`** - Shared base models and utilities:
- `BasicPage` - Simple content page model
- `SocialLink` - Snippet for social media links
- `MailRecipients` - Site-wide settings for email recipients
- Template tags and filters used across apps

**`concerts`** - Concert management:
- `ConcertsPage` - Landing page with archive filtering and pagination
- `ConcertPage` - Individual concert with date, location, ticket/FB links
- `Location` - Snippet for venue information
- Automatically splits upcoming vs. archived concerts based on `concert_date`

**`blog`** - Blog functionality:
- `BlogIndexPage` - Lists all blog posts
- `BlogPage` - Individual blog post with publication date and image

**`guides`** - Step-by-step rehearsal guides:
- `GuidesIndexPage` - Landing page
- `GuidePage` - Guide with ordered steps (uses Wagtail's Orderable)
- `Step` - Individual guide step with title and description

**`home`** - Landing page:
- `LandingPage` - Homepage with featured concerts and rehearsal info
- Pulls 3 most recent blog posts automatically

**`contact`** - Contact form:
- `ContactPage` - Page with contact form and contact details
- `ContactDetail` - Orderable contact information items with FontAwesome icons
- Integrated reCAPTCHA validation

**`search`** - Wagtail search functionality

### Template Structure
- `concertzaak/templates/` - Base templates (base.html, navigation.html, error pages)
- Each app has its own `templates/` subdirectory for app-specific templates
- Base template includes Google Tag Manager, Analytics, Facebook Pixel

### URL Routing
- `/admin/` - Wagtail CMS admin
- `/django-admin/` - Django admin
- `/documents/` - Wagtail documents
- `/search/` - Search functionality
- All other URLs handled by Wagtail's page serving mechanism

## Development Patterns

### Page Models
All content pages inherit from Wagtail's `Page` model. When creating new page types:
- Define `content_panels` for admin interface
- Use `parent_page_types` and `subpage_types` to control page hierarchy
- Override `get_context()` to add custom context variables

### Snippets
Reusable content pieces (like `Location`, `SocialLink`) use `@register_snippet` decorator.

### Rich Text Fields
Most content fields use `RichTextField` with controlled features list (e.g., `['h2', 'h3', 'bold', 'italic', 'link', 'image', 'ul']`).

### FontAwesome Icons
Contact details and social links reference FontAwesome icons by class name. Users find icons at https://fontawesome.com/

### Localization
- Language: Dutch (Belgium) - `nl-BE`
- Timezone: `Europe/Brussels`
- UI text, field names, and help text should be in Dutch

## Media Files
User-uploaded media stored in `media/` directory (not in git). Static files collected to `static/` directory during deployment.
