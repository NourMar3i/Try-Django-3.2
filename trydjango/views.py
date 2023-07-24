"""
render html
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article 
from django.views.generic import TemplateView
import random
# def home_view(request, *args, **kwargs):

#     article_obj = Article.objects.all().first()
#     article_queryset = Article.objects.all()
#     context = {
#         "object_list": article_queryset,
#         "object": article_obj,
#     }
#     HTML_STRING = render_to_string("home-view.html",context = context)

#     #return HttpResponse(HTML_STRING)
#     return render(request, "home-view.html", context=context)
class HomeView(TemplateView):
    template_name = "home-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_obj = Article.objects.first()
        article_queryset = Article.objects.all()
        context["object_list"] = article_queryset
        context["object"] = article_obj
        return context

