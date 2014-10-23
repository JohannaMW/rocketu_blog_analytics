from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/(\d+)/$', 'blog.views.post', name='post'),
    url(r'^posts/(\d+)/$', 'blog.views.post_list', name='post_list'),
    url(r'^analytics/$', TemplateView.as_view(template_name='analytics.html'), name='analytics'),
    url(r'^page/(\d+)/$', 'blog.views.page_view', name='page'),
    url(r'^error/$', 'blog.views.error', name='error'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)