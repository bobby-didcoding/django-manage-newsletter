from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import NewsLetter
from django.http import Http404
from django.conf import settings


'''
Check for an unsubscribe dict in settings
'''
try:
	reason_dict = settings.UNSUBSCRIBE_DICT
except AttributeError:
	reason_dict = {}


'''
Newletter conf view
Is used to handel news letter unsubscribe calls
Can also be used as the news letter success url
'''
class NewsLetterView(TemplateView):

	try:
		template_name = settings.NL_REDIRECT_HTML
	except AttributeError:
		template_name = "newsletter/news_letter.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		email = self.request.GET.get("email", None)
		reason = self.request.GET.get("reason", None)
		token = self.request.GET.get("token", None)
		context["sub"] = True

		if email and reason and token:
			try:
				reason_text = reason_dict[reason]
			except KeyError:
				reason_text = "Not specified"

			if token:
				try:
					nl_object = NewsLetter.objects.get(email = email.lower(), token = token)
					nl_object.is_active = False
					nl_object.reason = reason_text
					nl_object.save()
					context["sub"] = False

				except NewsLetter.DoesNotExist:
					raise Http404("New letter subscription not found")
			else:
				raise Http404("New letter subscription not found")

		
		return context