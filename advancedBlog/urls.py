from django.contrib import admin, sitemaps
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from Blog.sitemaps import PostSitemap

sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls',namespace='blog')),
    path('sitemap.xml/', sitemap,{'sitemaps':sitemaps},name="django.contrib.sitemaps.views.sitemap"),
]
