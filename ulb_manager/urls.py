from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from backend.urls import urlpatterns as qiitalist_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^qiita/', include(qiitalist_url)),
]

urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^__webpack_hmr', RedirectView.as_view(url='0.0.0.0:8080/__webpack_hmr'))
]
