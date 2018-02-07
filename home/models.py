from __future__ import unicode_literals
from django.db import models
from closuretree.models import ClosureModel

class Node(ClosureModel):
    name = models.CharField(max_length=24)
    parent = models.ForeignKey('self', related_name='children', null=True)

