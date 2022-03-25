from django.urls import path
from django.views.generic import TemplateView

from .views import InventoryAdd, InventoryDelete, InventoryEdit, InventoryList,PreviewAct

urlpatterns=[
    path(r'active-products/',InventoryList.as_view(),name='inventory'),
    path(r'active-products/product/<int:pk>/',PreviewAct.as_view(),name='previewact'),
    path(r'add-new-product/',InventoryAdd.as_view(),name='inventoryadd'),
    path(r'active-products/<int:id>/',InventoryEdit.as_view(),name='inventoryedit'),
    path(r'inventorydelete/<int:id>/',InventoryDelete.as_view(),name='inventorydelete'),


   
    
]
