from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "todo/index.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    fields = "__all__"
    template_name = "todo/task_form.html"


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    fields = "__all__"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def toggle_assign(request, pk):
    task = Task.objects.get(id=pk)
    if task.in_process is True:
        task.in_process = False
        task.save()
    else:
        task.in_process = True
        task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))




