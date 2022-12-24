from django.forms import ModelForm
from .models import Issued


class IssueForm(ModelForm):
    class Meta:
        model = Issued