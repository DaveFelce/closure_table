import os
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..' )
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../closure_table')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "closure_table.settings")
django.setup()

from home.models import Node

if __name__ == '__main__':
    a = Node.objects.create(name='A')
    b = Node.objects.create(name='B', parent=a)
    c = Node.objects.create(name='C', parent=b)
    d = Node.objects.create(name='D', parent=b)

