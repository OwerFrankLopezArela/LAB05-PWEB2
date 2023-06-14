from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_post/', views.newPost, name = "new_post" ),
    path('post/<int:id>', views.post, name = "post"),
    path('edit_post/<int:id>', views.editPost, name = "edit_post"),
    path('delete_post/<int:id>', views.deletePost, name = "delete_post")
]
