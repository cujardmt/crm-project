from unittest import TestCase
from django.contrib.auth.models import User
from django.db import transaction
from django.db.utils import IntegrityError, OperationalError


class UniqueConstraintTest(TestCase):

    def success_if_username_is_successfully_inserted_fail_if_not_successful(self):
        current_row_count = User.objects.count()
        try:
            User.objects.create_user(username='testusers', email='test@example.com', password='testpassword')
        except IntegrityError:
            pass
        except OperationalError:
            pass

        new_row_count = User.objects.count()
        self.assertGreater(new_row_count,
                           current_row_count,
                           f'current row count {current_row_count} ---- new row count {new_row_count}')

    def test_IntegrityError_is_raised_if_username_is_not_unique(self):
        # Try to create another user with the same username, and capture the expected IntegrityError
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                User.objects.create_user(username='testusers', email='test@example.com', password='testpassword')
