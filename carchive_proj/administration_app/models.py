from django.db import models
import re
import bcrypt
# Create your models here.

class AdminManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = " your password should be at least 8 characters"

        if len(postData['name']) < 2:
            errors["name"] = "Showroom name should be at least 2 characters"

        if len(postData['license_number']) != 9:
            errors["license_number"] = "license_number should be 9 characters"

    
        # if Admin.objects.filter(email = postData['email']).exists():
        #     errors['email'] = ("Email already exists, try logging in.")


        #this is for add showroom and edit showroom

            
        return errors




class Admin(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = AdminManager()