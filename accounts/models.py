import geocoder
from django.db import models
from django.contrib.auth.models import User


mapbox_access_token = 'pk.eyJ1IjoiaGFyc2hzdXJlbGEiLCJhIjoiY2xub3k5OGYzMGh2cjJucGYwZzB1djZqYiJ9.ZTcoON8tDDETT6I0AUwfHQ'                                                            
class Address(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     g = geocoder.mapbox(self.address, key=mapbox_access_token)
    #     g = g.latlng  # returns => [lat, long]
    #     self.lat = g[0]
    #     self.long = g[1]
    #     return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.userId.username

class category(models.Model):
    catName = models.CharField(max_length=50)
    def __str__(self):
        return self.catName
    

class Supplier(models.Model):
    gstNo =  models.CharField( max_length=50)
    gstImg = models.FileField(upload_to="gstImg")
    mobileNo = models.IntegerField()
    shopName = models.CharField( max_length=50)
    shopImg = models.ImageField( upload_to="shopImg")
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    catId = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.shopName
    

class Customer(models.Model):
    mobileNo = models.IntegerField(blank=True,null=True)
    userId = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.userId.username
    

class Tender(models.Model):
    catId = models.ForeignKey(category,on_delete=models.CASCADE)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fullFilled = models.BooleanField(default=False)

    def __str__(self):
        return self.customerId.userId.username
    

class TenderDetails(models.Model):
    productName = models.CharField( max_length=100)
    qty = models.IntegerField()
    tenderId = models.ForeignKey("Tender",related_name="tender", on_delete=models.CASCADE)

    def __str__(self):
        return self.productName
  
class Product(models.Model):
    name = models.CharField( max_length=100)
    qtyInStock = models.IntegerField()
    price = models.IntegerField()
    proImg =  models.ImageField( upload_to="Product_Img")
    supplierId = models.ForeignKey(Supplier,  on_delete=models.CASCADE)
    catId = models.ForeignKey(category,on_delete=models.CASCADE)  


class Quotation(models.Model):
    pricePerQty = models.FloatField()
    totalPrice = models.FloatField()
    tender = models.ForeignKey(Tender,related_name='quotations', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quotation_status = models.BooleanField(default=False)



