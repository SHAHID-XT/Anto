from django.forms import ModelForm
from .models import Sample

class Sampleform(ModelForm):
    class Meta:
        model = Sample
        fields= ['name','email','gender','img','phone','radio']
        
        
        


