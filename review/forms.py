from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(max_length=100, label="Your Name", error_messages={
        "required": "Please input the name value!",
        "max_length": "Please enter a shorter name!!"
    })
    feedback = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
