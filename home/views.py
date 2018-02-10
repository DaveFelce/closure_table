from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Node

class Home(View):
    """Home page class-based view

    Args:
        View (:obj:Django View base class, required)

    """

    def get(self, request):
        """get http method: very simple home page
        """

        node = Node.objects.get(name='B')
        e = Node.objects.create(name='E', parent=node)
        e.delete(keep_parents=True)
        child_nodes = node.get_children()
        return render(request, 'home/index.html', {'child_nodes': child_nodes})