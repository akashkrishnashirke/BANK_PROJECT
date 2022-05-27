from django import forms
from .models import LoanApplicationModel

class LoanApplictionModelForm(forms.ModelForm):
    class Meta:
        model= LoanApplicationModel
        fields= '__all__'


    def clean_income(self):
        inputincome= self.cleaned_data['income']
        if inputincome<10000:
             raise forms.ValidationError('salary should be more than 10k')
        return inputincome
    def clean_name(self):
        obj=self.cleaned_data['name']
        if len(obj)<5:
            raise forms.ValidationError("name should be less thsan five")
        return obj




