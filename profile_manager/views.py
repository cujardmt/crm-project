from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .forms import ProfileForm
from .models import Profile


# Create your views here.
def view_profile(request):
    template = 'profile_manager/profile_form.html'
    user_id = request.session['user_id']
    email = request.session['email']
    last_name = request.session['last_name']
    print(f'User ID: {user_id} --- Email: {email} Last Name: {last_name}')

    try:
        # profile = Profile.objects.get(user_id=user_id, email=email, last_name=last_name)
        profile = get_object_or_404(Profile, user_id=user_id, email=email, last_name=last_name)
        print(f'Profile String: {profile.__str__()}')
    except Http404:
        profile = Profile(user_id=user_id, last_name=last_name, email=email)
        print(f'Profile not found. Creating one.')

    form = ProfileForm(request.POST or None, instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


def save_profile(request, profile_id=None):
    template = 'profile_manager/profile_form.html'
    profile = None
    msg = "Profile created successfully."

    if profile_id is not None and profile_id != '':
        profile = Profile.objects.get(id=profile_id)
        msg = "Changes saved successfully."

    context = {
        'profile': profile,
    }

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, msg)
        else:
            print(f'{form.errors}')
            context['form'] = form

    return render(request, template, context)


def delete_profile(request, profile_id):
    return HttpResponse("Delete profile view.")
