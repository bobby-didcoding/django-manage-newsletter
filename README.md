# diddemo-newsletter

Demo Newsletter is a Django app that manages your newsletter subscriptions

Quick start:


1) Add "newsletter" to your INSTALLED_APPS setting like this.

    INSTALLED_APPS = [
        ...
        'newsletter',
    ]

2) Include the polls URLconf in your project urls.py like this.

    path('', include('newsletter.urls', namespace="news")),

3) Run "python manage.py migrate" to create the NewsLetter models.



Optional settings:


1) NL_REDIRECT_HTML

	Defailts to 'news/news_letter.html'. You can overwrite this settings by adding 
	NL_REDIRECT_HTML = 'your_html_location' to your settings.py file.


2) UNSUBSCRIBE_DICT

	Defaults to {}. You can overwrite this setting by adding
	UNSUBSCRIBE_DICT = {
    	"1": "Your first unsubscribe reason",
    	"2": "Your second unsubscribe reason",
    	"3": "Your third unsubscribe reason",
    	"4": "Your forth unsubscribe reason"
	}, to your settings.py file.

	Note: "Not specified" will be used when KeyError is raised when processing an unsubscribe request

Note: More settings coming soon

Configuration:


Main model: NewsLetter
Model form: NewsLetterForm - the form has an email field only
TemplateTag: {% nl_unsubscribe email=user_email reason=your_reason_key %}


1) Code example:

	views.py:

		from django.views.generic.edit import FormView
		from newsletter.forms import NewsLetterForm

		class ExampleView(FormView):

			template_name = "example.html"
			form_class = NewsLetterForm
			success_url = "/news-letter"

			def form_valid(self, form):
				form.save()
				return super().form_valid(form)

	urls.py:

		from django.urls import path
		from . import views

		app_name = "your_app_name"

		urlpatterns = [
			path("example", views.ExampleView.as_view(), name="example"),


	example.html:

		<form class="your-classes" id="newsletterform" method="POST">
		  {% csrf_token %}
		  <input type="email" class="your-classes" placeholder="Your email address.."  id="{{form.email.id_for_label}}" name="{{form.email.name}}">
		  <button class="your-classes" type="submit">Subscribe</button>
		</form>


	Your email html:

	{% load news_tags %}
	<!DOCTYPE html>
	<html lang="en">

	<head>

	</head>


	<body>
	  ...

	     <a href="{% nl_unsubscribe email=email_address reason=reason_key %}">unsubscribe</a>

	  ...
	</body>

	</html>





