# Casual Labour Marketplace

The Casual Labour Marketplace is a Django-based web application designed to connect clients who need short-term services with casual workers. The system supports multiple user roles and provides a structured way to manage users, jobs, and administration.

## Features
- User account management
- Multiple user roles: Clients, Workers, and Administrators
- Modular Django apps for scalability
- Admin management panel
- Job posting and worker engagement (planned)

## Technology Stack
- Backend: Django (Python)
- Database: SQLite (development)
- Frontend: HTML, CSS, JavaScript (Django Templates)
- Version Control: Git & GitHub

## Project Structure
Casual_Labour_Marketplace/
- accounts/
- adminpanel/
- client/
- worker/
- config/
- manage.py

## Setup
1. Clone the repository
2. Create and activate a virtual environment
3. Install Django
4. Run migrations
5. Start the development server

## Development Notes
SQLite is used during development because it is lightweight, requires no configuration, and works well with Django’s default setup. The project is structured to allow an easy transition to MySQL or PostgreSQL in production.

## Status
This project is currently under active development and is intended for learning and practical implementation of Django concepts.
