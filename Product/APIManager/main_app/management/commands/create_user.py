import os
import traceback

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            pwd = os.environ["ZENTERIO_PWD"]
        except KeyError:
            traceback.print_exc()
            pwd = "zenterio"
        try:
            if len(pwd) == 0:
                pwd = "zenterio"
            User.objects.create_user("Zenterio", password=pwd)
        except:
            traceback.print_exc()
