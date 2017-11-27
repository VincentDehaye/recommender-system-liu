import os
import traceback

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_user("Zenterio",
                                     password=os.environ.get("ZENTERIO_PWD", "zenterio"))
        except:
            traceback.print_exc()
