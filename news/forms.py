from django import forms
from .models import News, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "style": "width: 100%; border-radius: 20px; padding: 10px; margin: 10px;",
                    "placeholder": "Izoh matni..."
                }
            )
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['views']
