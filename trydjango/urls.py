
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from accounts.views import login_view
from accounts.views import logout_view
from accounts.views import register_view
from articles import views
from .views import HomeView
from articles.views import ArticleDetailView,ArticleCreateView,ViewPDF

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', views.article_search_view),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/list/', views.listing ),
    path('pdf_down/',views.html_to_pdf,name="pdf_down"),
    path('pdf_view/',ViewPDF.as_view(),name="pdf_view"),


    path('admin/', admin.site.urls),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),

    path('articles/',include('articles.urls'))
]

urlpatterns += static(settings.MEDIA_URL, docuemnt_root=settings.MEDIA_ROOT)