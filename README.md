# YouTube Clone — Django

A YouTube-inspired video-sharing web application built with Django, HTML, CSS, and JavaScript. This project is part of my journey toward becoming a Full Stack Software Engineer, focusing on Django web application development — frontend templates and backend fundamentals together.

Djangoを使用して、YouTubeを参考にした動画共有Webアプリケーションを開発する学習プロジェクトです。PythonとDjangoによるフルスタック開発の基礎を実践的に学んでいます。

### Homepage

The homepage features a dark theme inspired by YouTube, including a sidebar with a custom "LipuTube" logo, a search bar, category filter chips, microphone and notification icons, and a database-driven video grid.

## Features

- YouTube-inspired dark homepage UI with custom LipuTube branding
- Sidebar navigation with Home, Trending, and Library
- Database-driven video grid — videos are stored in PostgreSQL using `Channel` and `VideoContent` models and rendered as cards with thumbnail, title, and channel name
- Category filter chips loaded from the database (`TagTitles`), sticky at the top while scrolling
- Videos wrap automatically, 3 per row on desktop
- Shorts section on the homepage
- Search interface with a microphone (voice search) button
- Responsive layout for desktop and mobile screens
- Django project structure with separate apps: `home`, `main`, `shorts`, and `video`
- Environment variable configuration using `.env`

*Note: This is a learning project. Videos are currently managed through the Django shell and pgAdmin. User authentication and video uploads are planned as future development.*

## Tech Stack

- **Language:** Python, HTML, CSS, JavaScript
- **Framework:** Django
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Tools:** Git, GitHub, VS Code, PyCharm
- **Configuration:** Environment variables using `.env`

## Project Structure

```text
Youtube_Clone/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
├── main/
├── shorts/
├── video/
├── screenshots/
│   └── youtube_homepage.jpg
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lipumehedi/Youtube_Clone.git
cd Youtube_Clone
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment in Windows Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using the variables required by your Django settings.

Example `.env.example`:

```env
SECRET_KEY=replace-with-your-own-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Make sure your settings are configured to read these variables and keep your actual `.env` file out of Git.

### 5. Run database migrations

Make sure PostgreSQL is running and your database (for example `youtube_clone`) has been created, then run:

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

## Security

- Keep `.env` and private secret keys out of version control.
- Use `.env.example` to document required environment variables.
- Do not commit virtual environments or local database files.

## Learning Goals

- Understand Django project and app structure.
- Practice URL routing, views, and templates.
- Learn database models and Django ORM.
- Improve frontend integration with Django.
- Practice Git and GitHub version control.
- Build practical projects for a Full Stack Software Engineer portfolio.

## About Me

I am an aspiring Full Stack Software Engineer based in Japan, learning Python, Django, PostgreSQL, SQL, HTML/CSS/JavaScript, and Git/GitHub.

I am interested in building practical web applications and improving my full stack development skills through hands-on projects.

- **GitHub:** [lipumehedi](https://github.com/lipumehedi)

## Disclaimer

This is an independent educational project inspired by YouTube's interface. It is not affiliated with or endorsed by YouTube or Google.
