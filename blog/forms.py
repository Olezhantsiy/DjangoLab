from django import forms
from .models import Comment

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  # Убираем 'name'
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий', 'rows': '3'}),
        }
        labels = {
            'comment': 'Комментарий',
        }

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) > 400:
            raise forms.ValidationError("Комментарий не должен превышать 400 символов.")
        return comment

