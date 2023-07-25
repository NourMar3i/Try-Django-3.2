from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import ArticleForms
from .models import Article, PDFS
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from django.views import View 
from xhtml2pdf import pisa
from django.core.files import File
from pathlib import Path
from django.core.files.base import ContentFile
from rest_framework import generics,viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# from .models import Location, Item
from .serializers import ArticleSerializer


# Create your views here.

def article_search_view(request):
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get("q") # <input type='text' name='q' />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)


# class ArticleSearchView(ListView):
#     template_name = "articles/detail.html"
#     model = Article

#     def get_queryset(self):
#         name = self.kwargs.get('q')
#         object_list = self.model.objects.all()
#         if name:
#             object_list = object_list.filter(id="2")
#         return object_list 

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForms
    template_name = "articles/create.html"
    success_url = '/articles/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def article_create_view(request):
#     form = ArticleForms(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         article_object = form.save()
#         context['form'] = ArticleForms()
#         # context['object'] = article_object
#         # context['created'] = True
#     return render(request, "articles/create.html", context=context)

# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(request, "articles/create.html", context=context)

# def article_detail_view(request, id=None):
#     article_obj = None
#     if id is not None:
#         article_obj = Article.objects.get(id=id)
#     context = {
#         "object": article_obj,
#     }
#     return render(request, "articles/detail.html", context=context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "object"
    pk_url_kwarg = "id"




def listing(request):
    p=request.GET
    paginate_by=p.get("paginate_by")
    article_list = Article.objects.all().order_by('id')
    if paginate_by is None:
        paginator = Paginator(article_list, 5)
    else:
        paginator = Paginator(article_list, paginate_by)
    _request_copy_1 = request.GET.copy()
    _request_copy_2 = request.GET.copy()
    page_parameter = _request_copy_1.pop('page', True) and _request_copy_1.urlencode()
    paginate_parameter = _request_copy_2.pop('paginate_by', True) and _request_copy_2.urlencode()
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print("PAGE: ", page_obj)
    return render(request,"articles/list.html",{"page_obj":page_obj,"paginator":paginator,"page_parameter":page_parameter,"paginate_parameter":paginate_parameter})

def render_to_pdf(template_src, context_dict=[]):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

data={
    "articles": Article.objects.all(),
    }

def html_to_pdf(request):
    template = get_template('pdf_view.html')  # Replace 'your_template.html' with your actual HTML template path
    context = {'articles': Article.objects.all()}  # Replace with the context data for your template

    html = template.render(context)
    result = BytesIO()

    # Create a PDF object
    pdf = pisa.CreatePDF(html, dest=result)

    if not pdf.err:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
        response.write(result.getvalue())

        # Save the PDF file to the model (Assuming you have a model called 'MyModel')
        my_model = PDFS()  # Replace 'MyModel' with your actual model name
        my_model.pdf_file.save('generated_pdf.pdf', File(result))

        return response

    return HttpResponse('Error generating PDF.')

class ViewPDF(DetailView):
    template_name = "pdf_view.html"

    def get(self, request, *args, **kwargs):
        pdf =render_to_pdf('pdf_view.html',data)
        return HttpResponse(pdf,content_type='application/pdf')
    
# class ItemList(generics.ListCreateAPIView):
#     serializer_class = ItemSerializer

#     def get_queryset(self):
#         queryset = Item.objects.all()
#         location = self.request.query_params.get('location')
#         if location is not None:
#             queryset = queryset.filter(location=location)
#         return queryset

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class ArticleDD(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=False)
    def show3(self,request):
        queryset = Article.objects.all()[:3]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# class LocationList(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer


# class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer