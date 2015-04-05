#encoding=utf-8
from django.db import models

# Create your models here.
class user_items_table(models.Model):
	userid = models.CharField('userId',max_length=50)
	userdisplayname = models.CharField('userDisplayName',max_length=50)
	password = models.CharField('password',max_length=20)
	realname = models.CharField('realName',max_length=50)
	sex = models.CharField('sex',max_length=10)
	email = models.EmailField('email',blank=True);
	items_tablename = models.CharField('itemTableName',max_length=100);

	def __str__(self):
		return '%s%s'%(self.userid,self.userdisplayname)


class ssl_table(models.Model):
	itemid = models.CharField('itemId',max_length=100)
	itemname = models.CharField('itemName',max_length=100)
	itemcostprice = models.IntegerField('itemCostPrice',default = 0)
	itemprice = models.IntegerField('itemPrice')
	itemsnum = models.IntegerField('itemsNum')
	itemimageurl = models.CharField('itemImageUrl',max_length=200)
	itemimagetable = models.CharField('itemImageTable',max_length=100)

class ssl_en_table(models.Model):
	itemid = models.CharField('itemId',max_length=100)
	itemname = models.CharField('itemName',max_length=100)
	itemcostprice = models.IntegerField('itemCostPrice')
	itemprice = models.IntegerField('itemPrice')
	itemsnum = models.IntegerField('itemsNum')
	itemimageurl = models.CharField('itemImageUrl',max_length=200)
	itemimagetable = models.CharField('itemImageTable',max_length=100)