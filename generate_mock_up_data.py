import random
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.management import call_command

import os
import django

from contacts_manager.models import Contact
from profile_manager.models import Profile

# This script should be run and used during development only

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_project.settings")
django.setup()

# 1. Reset the SQLite database
call_command("reset_db", "--noinput")

# 2. make migration files
call_command("makemigrations")

# 3. Create database tables
call_command("migrate")

# Delete all existing records in each model
# TODO if the database is reset, there's no record to be deleted!
# Organization.objects.all().delete()
Profile.objects.all().delete()
# Note.objects.all().delete()
# Project.objects.all().delete()
User.objects.all().delete()

# create super user
call_command("createsuperuser", "--username=admin", "--email=admin@crm.com")

# Initialize the Faker generator
fake = Faker()

Faker.seed(0)  # Set a seed for reproducibility

# Create 10 profiles with random data
profiles = []
for _ in range(10):
    username = fake.user_name()
    password = 'password'
    email = fake.email()
    last_name = fake.last_name()
    first_name = fake.first_name()

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        last_name=last_name,
    )

    profile = Profile.objects.create(
        user=user,
        first_name=first_name,
        last_name=user.last_name,
        email=user.email,
        phone=fake.phone_number(),
        address=fake.address(),
        created_at=timezone.now(),
        updated_at=timezone.now(),
    )

    profiles.append(profile)

# Create 1 to 3 contacts for each profile
for profile in profiles:
    num_contacts = random.randint(1, 5)
    for _ in range(num_contacts):
        contact = Contact.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
        )
        profile.contacts.add(contact)

print("Mockup data generated successfully.")
