from django.urls import path

from todo.views import IndexView, TaskUpdateView, TaskCreateView, TaskDeleteView, TagListView, TagCreateView, \
    TagUpdateView, TagDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create-task/", TaskCreateView.as_view(), name="create-task"),
    path("update-task/<int:pk>/", TaskUpdateView.as_view(), name="upd-task"),
    path("delete-task/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

]


app_name = "todo"