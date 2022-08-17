from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'index.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')
