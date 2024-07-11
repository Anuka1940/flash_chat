Blog App
Welcome to the Blog App! This is a simple yet powerful blog application built with Flask and MySQL, allowing users to create, manage, and read blog posts. This README will guide you through the setup and usage of the app.

Features
User authentication (registration and login)
Create, edit, and delete blog posts
Comment on posts
Responsive design
Search functionality
Technologies Used
Backend: Flask
Database: MySQL
Frontend: HTML, CSS, JavaScript, Bootstrap
Prerequisites
Python 3.x
MySQL
Virtualenv (recommended)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Anuka1940/flash_chat.git
cd blog-app
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the MySQL database:

Create a database named blog_app.
Create a user with appropriate permissions.
Update the database configuration in config.py:
python
Copy code
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/blog_app'
Run the database migrations:

bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:

bash
Copy code
flask run
The app will be available at http://127.0.0.1:5000.

Usage
Register a new account:

Navigate to /register and create a new user account.
Log in:

Navigate to /login and log in with your credentials.
Create a new post:

Once logged in, navigate to /new_post to create a new blog post.
Manage posts:

Edit or delete your posts from the post detail page.
Comment on posts:
View a post and add comments to engage with other users.
Configuration
config.py: Update configurations such as database URI, secret key, and other settings.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or support, please open an issue or contact me at [anukalateef@gmail.com].
