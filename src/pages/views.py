from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1> Hello World</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text":"This is about us",
		"my_number":123,
		"my_list":[123, 4373, 7847]
	}
# for item in [123, 5564, 9674]:
# 	my_context['item'] = item

	return render(request, "about.html", my_context)	

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1> Scoial page </h1>")