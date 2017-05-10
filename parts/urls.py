from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'parts'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^AI/$', views.AIView.as_view(), name='AI'),
    url(r'^BK/$', views.BKView.as_view(), name='BK'),
    url(r'^CL/$', views.CLView.as_view(), name='CL'),
    url(r'^DT/$', views.DTView.as_view(), name='DT'),
    url(r'^EC/$', views.ECView.as_view(), name='EC'),
    url(r'^EG/$', views.EGView.as_view(), name='EG'),
    url(r'^EX/$', views.EXView.as_view(), name='EX'),
    url(r'^FC/$', views.FCView.as_view(), name='FC'),
    url(r'^GH/$', views.GHView.as_view(), name='GH'),
    url(r'^IG/$', views.IGView.as_view(), name='IG'),
    url(r'^IC/$', views.ICView.as_view(), name='IC'),
    url(r'^IT/$', views.ITView.as_view(), name='IT'),
    url(r'^SL/$', views.SLView.as_view(), name='SL'),
    url(r'^SF/$', views.SFView.as_view(), name='SF'),
    url(r'^SP/$', views.SPView.as_view(), name='SP'),
    url(r'^TK/$', views.TKView.as_view(), name='TK'),
    url(r'^WG/$', views.WGView.as_view(), name='WG'),
    url(r'^MC/$', views.MCView.as_view(), name='MC'),
    url(r'^TM/$', views.TMView.as_view(), name='TM'),
    url(r'^(?P<pk>[0-9]+)/order_success/$', views.OrderSuccessView.as_view(), name='order_success'),
    url(r'^(?P<pk>[0-9]+)/order_page/$', views.OrderPage.as_view(), name='order_page'),
    url(r'^(?P<part_id>[0-9]+)/purchase/$', views.purchase, name='purchase'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)