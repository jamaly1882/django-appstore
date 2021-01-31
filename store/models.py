from django.db import models
from django.contrib.auth.models  import User




# Create your models here.

# Create your models here.
class Customer(models.Model):
	 user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	 name=models.CharField(max_length=200)
	 email=models.CharField(max_length=200)
	 



class Product(models.Model):
	 #user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	 name=models.CharField(max_length=200)
	 price =models.FloatField()
	 digital =models.BooleanField(default=False,blank=False)
	 image=models.ImageField(null=True,blank=True)
	 def __str__(self):
	 	   return self.name
	 @property
	 def imageURL(self):
	 	try:
	 	 	url=self.image.url
	 	except:
	 		 url=''
	 	return url
	 
class Order(models.Model):
	 #user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	 customer=models.ForeignKey(Customer,null=True, blank=True,on_delete=models.CASCADE)
	 date_ordered=models.DateTimeField( auto_now_add=True)
	 complete =models.BooleanField(default=False,blank=False)
	 transaction_id=models.IntegerField(primary_key=True,unique=True)
	 def __str__(self):
	 	   return self.transaction_id
	 @property
	 def get_cart_total(self):
	 	orderitems=self.orderitem_set.all()
	 	total=sum([item.get_total for item in orderitems])
	 	return total
	 @property
	 def shipping(self):
	 	shipping=False
	 	orderitems=self.orderitem_set.all()
	 	for i in orderitems:
	 		 if i.product.digital==False:
	 		     shipping=True
	 	return  shipping
	 	
	 @property
	 def get_cart_item(self):
	 	orderitems=self.orderitem_set.all()
	 	total=sum([item.quantity for item in orderitems])
	 	return total

class OrderItem(models.Model):
	 #user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	 product=models.ForeignKey(Product,null=True, blank=True,on_delete=models.CASCADE)
	 order=models.ForeignKey(Order,null=True, blank=True, on_delete=models.CASCADE)
	 quantity=models.IntegerField(default=0,blank=True)
	 date_added=models.DateTimeField(auto_now_add=True)
	 @property
	 def get_total(self):
	 	return self.product.price * self.quantity

	 

class ShippingAdress(models.Model):
	 #user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer,null=True, blank=True,on_delete=models.CASCADE)
	order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.CASCADE)
	address=models.CharField(max_length=200,null=True)
	city=models.CharField(max_length=200,null=True)
	zipcode=models.CharField(max_length=200,null=True)
	date_added=models.DateTimeField(auto_now_add=True)
