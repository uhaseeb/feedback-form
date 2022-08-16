from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review


def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            review = Review(user_name=form.cleaned_data['username'],
                            feedback=form.cleaned_data['feedback'],
                            rating=form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, 'index.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')
