from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from profile_manager.models import Profile


def create_contact(request, profile_id):
    template = 'contacts_manager/contact_form.html'
    profile = Profile.objects.get(id=profile_id)
    form = ContactForm()
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


def view_contact(request, profile_id, contact_id):
    template = 'contacts_manager/contact_form.html'
    profile = Profile.objects.get(id=profile_id)
    contact = profile.contacts.get(id=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    context = {
        'profile': profile,
        'contact': contact,
        'form': form,
    }

    return render(request, template, context)


def save_contact(request, profile_id, contact_id=None):
    template = 'contacts_manager/contact_form.html'
    profile = Profile.objects.get(id=profile_id)
    contact = None
    msg = "Contact created successfully."

    if contact_id is not None and contact_id != '':
        contact = profile.contacts.get(id=contact_id)
        msg = "Changes saved successfully."

    context = {
        'profile': profile,
        'contact': contact,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            profile.contacts.add(form.instance)
            messages.success(request, msg)
        else:
            context['form'] = form

    return render(request, template, context)


def delete_contact(request, profile_id, contact_id):
    profile = Profile.objects.get(id=profile_id)
    # TODO: Error handling here
    contact = profile.contacts.get(id=contact_id)
    contact.delete()
    messages.success(request, 'Contact was deleted successfully.')
    return redirect(f"/profile/{profile_id}")
