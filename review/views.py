from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView


class ReviewView(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = "index.html"
    success_url = "/thank-you"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, requests):
        review_id = requests.POST['review_id']
        requests.session['favorite_review'] = review_id
        return HttpResponseRedirect('reviews/' + review_id)
