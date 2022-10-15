from datetime import datetime
from time import strftime
from django.db import models
from administration_app.models import Admin
import re
import bcrypt
from datetime import datetime
# Create your models here.

class ShowroomManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        try:
            Showroom.objects.get(email=postData['email'])
        except:
            pass
        else:
            errors['email']='Email already exists choose another'

        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = " your password should be at least 8 characters"

        if len(postData['name']) < 2:
            errors["name"] = "Showroom name should be at least 2 characters"

        if len(postData['license_number']) != 9:
            errors["license_number"] = "license_number should be 9 characters"

        return errors

    def advanced_validator(self,postData):
        errors={}
        try:
            Showroom.objects.get(email=postData['email'])
        except:
            pass
        else:
            errors['email']='Email already exists choose another'

        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"

        if len(postData['name']) < 2:
            errors["name"] = "Showroom name should be at least 2 characters"

        if len(postData['license_number']) != 9:
            errors["license_number"] = "license_number should be 9 characters"

        return errors


class Showroom(models.Model):
    license_number=models.CharField(max_length=10)
    created_by=models.ForeignKey(Admin, related_name='showrooms',on_delete=models.CASCADE)
    name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    payment=models.CharField(max_length=45)
    objects=ShowroomManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




class BrandManager(models.Manager):
    def brand_validator(self, postData):
        errors = {}
        if len(postData["brand"]) < 1:
            errors["brand"] = " you need to add the brand name"
        return errors

class Brand(models.Model):
    name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BrandManager()



class BrandModelManager(models.Manager):
    def modelBrand_validator(self, postData):
        errors = {}
        if len(postData["model"]) < 1:
            errors["model"] = " you need to add the model name"
        return errors
class BrandModel(models.Model):
    brand=models.ForeignKey(Brand,related_name='models',on_delete=models.CASCADE)
    name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BrandModelManager()


class CarManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["vin"]) != 17:
            errors["vin"] = " VIN is 17 characters (Vehicle Identification Number)"


        if postData['prod_date']=='':
            errors["prod_date"] = " you need to provide the production date"


        try:
            if datetime.strptime(postData['prod_date'],'%Y-%m-%d')>datetime.today():
                errors["prod_date"] = " the car's production date should be in the past"
        except:
            errors["prod_date"]='Please add the production date'


        try:
            postData['color']
        except:
            errors['color']='Please choose a color'


        try:
            postData['brand']
        except:
            errors['brand']='Please choose a brand'


        try:
            postData['model']
        except:
            errors['model']='Please choose a model'

        try:
            Car.objects.get(vin=postData['vin'])
        except:
            pass
        else:
            errors['vin']='VIN already exists'


        return errors


class Car(models.Model):
    vin=models.CharField(max_length=17)
    showroom=models.ForeignKey(Showroom,related_name="cars",on_delete=models.CASCADE)
    model=models.ForeignKey(BrandModel,related_name='cars',on_delete=models.CASCADE)
    prod_date=models.DateField()
    color=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CarManager()





class DocumentTypeManager(models.Manager):
    def DocumentType_validator(self, postData):
        errors = {}
        if len(postData["doc_type"]) < 1:
            errors["doc_type"] = " you need to add the document type name"
        return errors
class DocumentType(models.Model):
    type=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=DocumentTypeManager()





class Document(models.Model):
    car=models.ForeignKey(Car,related_name='documents',on_delete=models.CASCADE)
    type=models.ForeignKey(DocumentType,related_name='documents',on_delete=models.CASCADE)
    doc=models.FileField(upload_to='documents/%Y/%m/%d/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.doc.delete()
        super().delete(*args,**kwargs)