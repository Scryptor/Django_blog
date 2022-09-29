"""igors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import blog_article, BlogView, blog_app
from aboutme.views import AboutMeView, aboutme_app
from comments.views import CommentsView
from django.conf.urls.static import static
from django.conf import settings
from igors_tools.views import puny
from rest_framework.routers import SimpleRouter

from prodmenu.views import prodmenu_app, ProdmenuView

router = SimpleRouter()
router.register('api/v1/posts', BlogView)
router.register('api/v1/about', AboutMeView)
router.register('api/v1/comments', CommentsView)
router.register('api/v1/food/prodmenu', ProdmenuView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("post/<int:article_id>", blog_article, name="article"),
    path('punyrl/', puny),
    path('aboutme/', aboutme_app, name="aboutmepage"),
    path('', blog_app, name="home"),
    path('prodmenu/', prodmenu_app, name="eater"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
