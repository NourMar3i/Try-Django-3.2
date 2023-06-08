"""
render html
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article 
import random
def home_view(request,*args,**kwargs):
    print(id)
    rand_id=random.randint(1,4)
    article_obj=Article.objects.get(id=rand_id)
    article_queryset = Article.objects.all()

    context = {
        "object_list":article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,

    }
    HTML_STRING = render_to_string("home-view.html",context = context)

    #return HttpResponse(HTML_STRING)
    return render(request, "home-view.html", context=context)
