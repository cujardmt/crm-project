from django.test import TestCase
from django.contrib.auth.models import User
from contacts_manager.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        # Create a User object for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_should_add_new_profile(self):
        # Test creating a new profile
        current_profile_count = Profile.objects.count()

        profile = Profile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone='1234567890',
            organization=None,
            address='123 Main St'
        )

        new_profile_count = Profile.objects.count()
        print(f"Last Name: {profile.last_name} First Name :{profile.first_name}")
        self.assertGreater(new_profile_count, current_profile_count)

    def test_should_existing_read_profile(self):
        # Test reading a profile
        profile = Profile.objects.create(
            user=self.user,
            first_name='Jane',
            last_name='Smith',
            email='jane@example.com'
        )
        retrieved_profile = Profile.objects.get(id=profile.id)
        self.assertEqual(retrieved_profile.first_name, 'Jane')
        self.assertEqual(retrieved_profile.email, 'jane@example.com')

    def test_should_update_existing_profile(self):
        # Test updating a profile
        profile = Profile.objects.create(
            user=self.user,
            first_name='Alice',
            last_name='Johnson',
            email='alice@example.com'
        )
        profile.first_name = 'Alicia'
        profile.save()
        updated_profile = Profile.objects.get(id=profile.id)
        self.assertEqual(updated_profile.first_name, 'Alicia')

    def test_raise_DoesNotExist_if_profile_does_not_exist(self):
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(id=100)

    def test_raise_DoesNotExist_if_profile_deleted_does_not_exist(self):
        # Test deleting a profile
        profile = Profile.objects.create(
            user=self.user,
            first_name='Bob',
            last_name='Brown',
            email='bob@example.com'
        )
        profile_id = profile.id
        profile.delete()

        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(id=profile_id)
