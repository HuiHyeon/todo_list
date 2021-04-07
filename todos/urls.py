from django.conf.urls import include, url
from django.urls import re_path
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from todos import views

todo_router = routers.DefaultRouter()
todo_router.register(r'todos', views.TodoViewSet, basename="todo")
commnet_router = nested_routers.NestedSimpleRouter(
    todo_router, r'todos', lookup="todo")
commnet_router.register(r'comments', views.CommentViewSet, basename="comment")


urlpatterns = [
    re_path('^', include(todo_router.urls)),
    re_path('^', include(commnet_router.urls)),
]

# from django.urls import path
# from django.conf.urls import url
# from todos import views

# urlpatterns = [
#     path('todos', views.todo_list),
#     path('todos/<int:pk>', views.todo_detail),
#     # path('todos/<int:pk>/comments', views.comment_list),
#     # path('todos/<int:pk>/comments/<int:pk>', views.comment_detail),
# ]
