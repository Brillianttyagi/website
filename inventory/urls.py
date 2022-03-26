from django.urls import path
from .views import InventoryAdd, InventoryDelete, InventoryEdit, InventoryList,PreviewAct,InventoryListSearch,InventoryListOnline,InventoryUnistOnline

urlpatterns=[
    path(r'active-products/',InventoryList.as_view(),name='inventory'),
    path(r'add-new-product/',InventoryAdd.as_view(),name='inventoryadd'),
    path(r'active-products/<int:id>/',InventoryEdit.as_view(),name='inventoryedit'),
     path(r'active-products/product/<int:pk>/',PreviewAct.as_view(),name='previewact'),
    path(r'inventorydelete/<int:id>/',InventoryDelete.as_view(),name='inventorydelete'),
    path(r'active-products/search/',InventoryListSearch.as_view(),name='inventorysearch'),
    path(r'list-online/<int:id>/',InventoryListOnline.as_view(),name='inventorylist'),
    path(r'unlist-online/<int:id>/',InventoryUnistOnline.as_view(),name='inventorylist'),

   
    
]
