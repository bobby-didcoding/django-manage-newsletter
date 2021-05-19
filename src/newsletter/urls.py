from django.urls import path
from . import views

app_name = "newsletter"

urlpatterns = [

	path("news-letter", views.NewsLetterView.as_view(), name="news-letter"),
]