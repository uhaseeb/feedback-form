from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
        label = {
            "user_name": "Your Name",
            "feedback": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                            "required": "You must enter the name!",
                            "max_length": "Please enter a shorter name"
                        }
        }
