from django.test import TestCase

from profile_manager.models import Profile


class ContactModelTest(TestCase):
    def setUp(self):
        contact = Profile.objects.get(last_name="Williams").contacts.get(id=1)

    def test_display_contact_with_id_1(self):
        contact = Profile.objects.get(last_name="Williams").contacts.get(id=1)
        print(f"Last Name: {contact.last_name} First Name : {contact.first_name}")
        self.assertEqual('David', contact.last_name)
        self.assertEqual('Estrada', contact.last_name)
