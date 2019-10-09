from restaurant import views
from django.urls import path

##...

urlpatterns = [
    path('api/plats/', views.plat_list),
    path('api/plats/(?P<pk>[0-9]+)', views.plat_detail),

]