try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less then 1.4
    from django.conf.urls.defaults import url, patterns

from . import views

urlpatterns = patterns("",
    url(r"^$", views.su_login, name="su-login"),
    url(r"^logout$", views.su_logout, name="su-logout"),
)
