import django
django.setup()

from django.contrib.auth.models import User

from testapp.models import UserList


UserList.objects.filter(users__overlap=User.objects.all().values_list('id', flat=True)).count()
