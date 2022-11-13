from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name="index-blog"),
    path('listpost/', ListPost.as_view(), name="list-post"),
    path('createpost/', CreatePost.as_view(), name="create-post"),
    path('detailpost/<int:pk>/', DetailPost.as_view(), name="detail-post"),
    path('updatepost/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),
    path('blog/login/', BlogLogin.as_view(), name="blog-login"),
    path('blog/logout/', BlogLogout.as_view(), name="blog-logout"),
]