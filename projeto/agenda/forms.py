from django import forms

class FormItemAgenda(forms.Form):
    titulo = forms.CharField(max_length=80)
    data = forms.DateField(
        widget = forms.DateInput(format='%d/%m/%Y'),
        input_formats = ['%d/%m/%y', '%d/%m/%Y'])
    hora = forms.TimeField()
    descricao = forms.CharField()
    local = forms.CharField()
