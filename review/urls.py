from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReviewView.as_view(), name="review_index"),
    path('thank-you', views.ThankyouView.as_view(), name='thankyou'),
    path('reviews', views.ReviewsListView.as_view(), name='all_reviews'),
    path('favorite', views.AddFavoriteView.as_view(), name='favorite_review'),
    path('reviews/<int:pk>', views.SingleReviewView.as_view(), name='single_review')
]
