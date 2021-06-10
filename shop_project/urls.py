#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/accounts/', include('user.urls')),
# ]
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/accounts/', include('user.urls')),
    path('api/v1/products/', include('product.urls')),

]

