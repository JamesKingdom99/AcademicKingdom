from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import PostForms

urlpatterns = [
                url(r'^$', ListView.as_view(
                                    queryset=PostForms.objects.all().order_by()[:25],
                                    template_name="blog/blog.html"), name='blog'),

                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = PostForms,
                                    template_name="blog/post.html")),
                url(r'postForm', views.postform, name='postform')
            ]
