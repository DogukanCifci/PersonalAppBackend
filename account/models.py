from django.db import models
from django.contrib.auth.models import User

class Profile(User) :
    about = models.TextField()
    image = models.ImageField(upload_to='account/', blank=True, null=True)


