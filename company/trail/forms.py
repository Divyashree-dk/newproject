from django import forms
from trail.models import *
from django.forms.models import inlineformset_factory


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name','adress','ph')
MaterialsFormset = inlineformset_factory(Company, Agent, fields=('agent_name','adress','contact_num'),can_delete=False,extra=3)


class AgentForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields = ('agent_name','adress','contact_num')
