from django import forms
from .models import Estoque

class estoqueForm(forms.ModelForm):
        nome = forms.CharField(widget=forms.TextInput(attrs={'':'','class': 'form-control',}))

        preco = forms.IntegerField(widget=forms.NumberInput(attrs={'':'','class': 'form-control',}))
        
        validade = forms.DateField(widget=forms.SelectDateWidget(attrs={'':'','class': 'form-control',}))
        
        tipo= forms.CharField(widget=forms.TextInput(attrs={'':'','class': 'form-control',}))
        
        familia = forms.CharField(widget=forms.TextInput(attrs={'':'','class': 'form-control',}))
        
        quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'':'','class': 'form-control',}))
        
        descricao = forms.CharField(widget=forms.Textarea(attrs={'required': False, '':'','class': 'form-control',}))

        class Meta:        
                model=Estoque
                fields = [
                        "nome",
                        "preco",
                        "validade",
                        "tipo",
                        "familia",
                        "quantidade",
                        "descricao",
                ]


# '''
# class ExampleForm(forms.Form):
        
#         helper = FormHelper()
#         helper.form_id = 'id-exampleForm'
#         helper.form_class = 'blueForms'
#         helper.form_method = 'get'
#         helper.form_action = '/'
#         helper.layout = Layout(
#                 Div(),
#                 Field('field_name', css_class="black-fields"),
#                 Field('password', id="password-field", css_class="passwordfields", title="Explanation")
#         #Submit('submit', 'Submit', css_class="btn btn-success btn-block")
#         )
#        # helper.add_input(Submit('submit', 'Submit', css_class="btn btn-success btn-block"))
# --------------------------------------------------------------------------------------------------
#         like_website = forms.TypedChoiceField(
#         label = "Do you like this website?",
#         choices = ((1, "Yes"), (0, "No")),
#         coerce = lambda x: bool(int(x)),
#         widget = forms.RadioSelect,
#         initial = '1',
#         required = True,
#         )

#         favorite_food = forms.CharField(
#         label = "What is your favorite food?",
#         max_length = 80,
#         required = True,
#         )
#         #AppendedText('nome', 'appended text to show')
#         favorite_color = forms.CharField(
#         label = "What is your favorite color?",
#         max_length = 80,
#         required = True,
#         )

#         favorite_number = forms.IntegerField(
#         label = "Favorite number",
#         required = False,
#         )

#         notes = forms.CharField(
#         label = "Additional notes or feedback",
#         required = False,
#         )
# '''



# ''' class estoqueForm(forms.ModelForm):
#         helper = FormHelper()
#         helper.form_show_labels = False  
#         helper.form_id = 'id-exampleForm'
#         helper.form_method = 'GET'
#         helper.render_required_fields=False
#         #helper.field_class = "form-control"
#         #AppendedText('nome', 'appended text to show')
#         helper.add_input(Submit('submit', 'Adicionar', css_class = "btn btn-primary btn-block")) 
        
#         class Meta:        
#                 model=Estoque
#                 fields = [
#                         "nome",
#                         "preco",
#                         "validade",
#                         "tipo",
#                         "familia",
#                         "quantidade",
#                         "descricao",
#                 ]



#     class Meta:
#         model = Estoque
        
#         nome = forms.CharField(label = "nome", max_length = 80, required = True,)
#         preco = forms.IntegerField(label = "preço", required = True,)
#         validade = forms.DateField(label = "prazo", required = True,)
#         tipo = forms.CharField(label = "tipo", max_length = 100, required = False,)
#         Familia = forms.CharField(label = "familia", max_length = 80, required = True,)
#         quantidade = forms.IntegerField(label = "nome", required = True,)
#         descricao = forms.CharField(label = "descrição", max_length = 100, required = False,)
#         */


       
#         fields = [
#                 "nome",
#                 "preco",
#                 "validade",
#                 "tipo",
#                 "familia",
#                 "quantidade",
#                 "descricao",
# ]
# '''