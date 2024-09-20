import os
# from django.contrib.auth import get_user_model

# User = get_user_model()
# User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')


from django.db import IntegrityError
from django.contrib.auth.models import User

try:
    superuser = User.objects.create_superuser(
        username=os.getenv('SUPERUSER_USERNAME'),
        email=os.getenv('SUPERUSER_EMAIL'),
        password=os.getenv('SUPERUSER_PASSWORD'))
    superuser.save()
except IntegrityError:
    print(f"Super User with username {os.getenv('SUPERUSER_USERNAME')} already exist!")
except Exception as e:
    print(e)