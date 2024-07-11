#!/usr/bin/python3
from flash_chat import app, db
from flash_chat.models import User


with app.app_contenxt():
    user = User.querry.filter_by(username='anuka1940').first()

if user:
    print(f"{user.username}")
else:
    print("user does not exist")

