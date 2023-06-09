"""
render html
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article 
import random
def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin" # hard coded
    random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
    HTML_STRING = render_to_string("home-view.html",context = context)

    #return HttpResponse(HTML_STRING)
    return render(request, "home-view.html", context=context)