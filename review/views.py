from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "index.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context


class ReviewsListView(ListView):
    template_name = 'reviews.html'
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = 'single-review.html'
    model = Review
    context_object_name = 'review'
