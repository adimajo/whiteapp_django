from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from loguru import logger

SUPERUSER_ = 'Superuser '


class Command(BaseCommand):  # pragma: no cover
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin's username")
        parser.add_argument('--email', help="Admin's email")
        parser.add_argument('--password', help="Admin's password")

    def handle(self, *args, **options):
        logger.info('Trying to create a superuser.')
        user = get_user_model()
        if not user.objects.filter(username=options['username']).exists():
            logger.info(SUPERUSER_ + options['username'] + ' does not exist. Creating...')
            user.objects.create_superuser(username=options['username'],
                                          email=options['email'],
                                          password=options['password'])
            logger.info(SUPERUSER_ + options['username'] + ' created.')
        else:
            logger.info(SUPERUSER_ + options['username'] + ' already exists.')
