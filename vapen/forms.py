# from django import forms

# model_type = (
#     'm4','pistols','smg','shotgun','machingeguns','other','custom'

# )


# class ModelForm(forms.Form):
#     model_type1 = forms.ChoiceField(choices = model_type)



from django import forms 

# iterable 
GEEKS_CHOICES =( 
	("1", "One"), 
	("2", "Two"), 
	("3", "Three"), 
	("4", "Four"), 
	("5", "Five"), 
) 

# creating a form 
class GeeksForm(forms.Form): 
	geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES) 
