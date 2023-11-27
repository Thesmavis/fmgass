from django.urls import path
from . import views

urlpatterns = [
    path('POST/api/vendors/',views.vendorview_POST.as_view(),name='create'),
    path('GET/api/vendors/',views.vendorview_GET.as_view(),name='getall'),
    path('GET/api/vendors/<int:id>/',views.vendorview_GET.as_view(),name='byid'),
    path('PUT/api/vendors/<int:id>/',views.vendorview_PATCH.as_view(),name='patch'),
    path('DELETE/api/vendors/<int:id>/',views.vendorview_DELETE.as_view(),name='delete'),

    path('POST/api/purchase_orders/',views.poview_POST.as_view(),name='create1'),
    path('GET/api/purchase_orders/',views.poview_GET.as_view(),name='getall1'),
    path('GET/api/purchase_orders/<int:id>/',views.poview_GET.as_view(),name='byid1'),
    path('PUT/api/purchase_orders/<int:id>/',views.poview_PATCH.as_view(),name='patch1'),
    path('DELETE/api/purchase_orders/<int:id>/',views.poview_DELETE.as_view(),name='delete1'),
    
    path('POST/api/purchase_orders/<int:id>/acknowledge/',views.performance_calculation1.as_view()),
    path('GET/api/vendors/<int:id>/performance/',views.perform_get.as_view()),

]