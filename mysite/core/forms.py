from django.forms import ModelForm
from .models import Atendimento

class Atedimento(ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'
