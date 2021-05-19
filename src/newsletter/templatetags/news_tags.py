from django import template
from newsletter.models import NewsLetter
from newsletter.views import reason_dict

register = template.Library()

@register.simple_tag
def nl_unsubscribe(**kwargs):

	email = kwargs.get("email")
	reason = kwargs.get("reason")

	if email:

		nl_object = NewsLetter.objects.get(email = email.lower())

		if reason:

			try:
				reason_text = reason_dict[reason]
			except KeyError:
				reason_text = "Not specified"

			url = nl_object.get_absolute_url()

			params = nl_object.get_params

			return f'{url}{params}&reason={reason}'
	
	return None
