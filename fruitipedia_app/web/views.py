from django.shortcuts import render, redirect

from fruitipedia_app.web.forms import ProfileCreateForm, EditFruitForm, CreateFruitForm, DeleteFruitForm, \
	ProfileEditForm
from fruitipedia_app.web.models import Profile, Fruit


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None
def index(request):
	profile=get_profile()
	context={
		'profile':profile,
	}

	return render(request, 'index.html', context)

def dashboard(request):
	profile=get_profile()
	fruits=Fruit.objects.all()

	context={
		'fruits': fruits,
		'profile': profile
	}

	return render(request, 'dashboard.html', context)
def create_fruit(request):
	profile=get_profile()
	if request.method == 'GET':
		form = CreateFruitForm()
	else:
		form = CreateFruitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dasboard')
	context = {
		'form': form,
		'profile': profile
	}

	return render(request, 'fruits/create-fruit.html', context)

def fruit_details(request, pk):
	profile=get_profile()
	fruit=Fruit.objects.filter(pk=pk).get()
	context={
		'fruit':fruit,
		'profile':profile
	}
	return render(request, 'fruits/details-fruit.html', context)

def edit_fruit(request, pk):
	profile = get_profile()
	fruit=Fruit.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = EditFruitForm(instance=fruit)
	else:

		form = EditFruitForm(request.POST, instance=fruit)
		if form.is_valid():
			form.save()
			return redirect('dasboard')
	context = {
		'form': form,
		'fruit': fruit,
		'profile': profile
	}
	return render(request, 'fruits/edit-fruit.html', context)

def delete_fruit(request, pk):
	profile=get_profile()
	fruit=Fruit.objects.filter(pk=pk).get()
	if request.method == 'GET':
		form = DeleteFruitForm(instance=fruit)
	else:
		form = DeleteFruitForm(request.POST, instance=fruit)
		if form.is_valid():
			form.save()
			return redirect('dasboard')
	context = {
		'form': form,
		'fruit': fruit,
		'profile': profile
	}

	return render(request, 'fruits/delete-fruit.html', context)

def create_profile(request):
	if request.method == 'GET':
		form = ProfileCreateForm()
	else:
		form = ProfileCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dasboard')
	context = {
		'form': form,
	}
	return render(request, 'profiles/create-profile.html', context)

def profile_details(request):
	profile=get_profile()
	posts=Fruit.objects.count()
	context={
		'profile':profile,
		'posts':posts
	}

	return render(request, 'profiles/details-profile.html', context)

def edit_profile(request):
	profile = get_profile()
	if request.method == 'GET':
		form = ProfileEditForm(instance=profile)
	else:
		form = ProfileEditForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile-details')
	context = {
		'form': form,
		'profile': profile
	}
	return render(request, 'profiles/edit-profile.html', context)

def delete_profile(request):
	profile=get_profile()
	if request.method=='POST':
		Fruit.objects.all().delete()
		profile.delete()
		return redirect('index')
	return render(request, 'profiles/delete-profile.html')
