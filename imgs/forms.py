from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('caption', 'image')

class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))		