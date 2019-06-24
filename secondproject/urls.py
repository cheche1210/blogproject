
from django.contrib import admin
from django.urls import path,include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),#path converter 숫자를 통해 숫자로 계층적인 url을?????
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
