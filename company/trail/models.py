from django.db import models
from django.contrib.auth.models import User





class Company(models.Model):
	name = models.CharField(max_length=20,null=False, blank=False)
	adress = models.CharField(max_length=20,null=False, blank=False)
	ph = models.IntegerField(null=True, blank=True)

	class meta:
		ordering = ('-salary',)

	def __str__(self):
		return  self.name

class Agent(models.Model):
	agent_name = models.CharField(max_length=20,null=False, blank=False)
	adress=models.CharField(max_length=20,null=False, blank=False)
	
	contact_num=models.IntegerField(null=True, blank=True)
	company= models.ForeignKey(Company, on_delete=models.CASCADE)

	

	def __str__(self):
		return  self.agent_name