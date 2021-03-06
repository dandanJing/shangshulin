#encoding=utf-8
from django.db import models 
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class user_items_table(models.Model):
	userid = models.CharField('userId',max_length=50, unique=True)
	userdisplayname = models.CharField('userDisplayName',max_length=50)
	password = models.CharField('password',max_length=20)
	realname = models.CharField('realName',max_length=50)
	sex = models.CharField('sex',max_length=10)
	email = models.EmailField('email',blank=True);
	items_tablename = models.CharField('itemTableName',max_length=100);

	def __str__(self):
		return '%s%s'%(self.userid,self.userdisplayname)

class ssl_table(models.Model):
	itemid = models.CharField('itemId',max_length=100, unique=True)
	itemname = models.CharField('itemName',max_length=100)
	itemcostprice = models.IntegerField('itemCostPrice',default = 0)
	itemprice = models.IntegerField('itemPrice')
	itemsnum = models.IntegerField('itemsNum')
	itemimageurl = models.CharField('itemImageUrl',max_length=200)
	lookCount = models.IntegerField('lookCount',default = 0)
	postTime = models.DateTimeField('postTime',default = datetime.now())
	lastEditTime = models.DateTimeField('lastEditTime',default = datetime.now())
	isBlock = models.BooleanField('isBlock', default=True)
	username = models.CharField('username',max_length=100,default="尚书林")
	feature = models.CharField('feature',max_length=100,default="全新")
	itemType = models.CharField('itemType',max_length=20,default="")

class ssl_users(AbstractUser):
	mobilephone = models.CharField('mobilephone',max_length=20,default="")
	qq = models.IntegerField('qq',default=0)
	nickname = models.CharField('nickname',max_length=20)
	is_student = models.BooleanField('is_student',default=True)

	def __str__(self):
		return "username:%s\tphone:%s\temail:%s\t"%(self.username,self.mobilephone,self.email)
	
	def is_valid_user(self):
		return False

class ssl_images_table(models.Model):
	itemid = models.CharField('itemId',max_length=100)
	itemimageurl = models.CharField('itemImageUrl',max_length=200)