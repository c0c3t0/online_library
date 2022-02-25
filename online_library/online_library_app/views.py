from django.shortcuts import render, redirect

from online_library.online_library_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, \
    CreateBookForm, EditBookForm
from online_library.online_library_app.models import Profile, Book


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == "POST":
        book_form = CreateBookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('home page')
    else:
        book_form = CreateBookForm()

    context = {
        'profile': get_profile(),
        'book_form': book_form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book_form = EditBookForm(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('home page')
    else:
        book_form = EditBookForm(instance=book)

    context = {
        'book': book,
        'book_form': book_form,
        'profile': get_profile(),

    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book,
        'profile': get_profile(),

    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home page')


def create_profile(request):
    profile = get_profile()
    if request.method == "POST":
        profile_form = CreateProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home page')
    else:
        profile_form = CreateProfileForm()
    context = {
        'profile': profile,
        'has_profile': False,
        'profile_form': profile_form,
    }

    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST, instance=get_profile())
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show profile')
    else:
        profile_form = EditProfileForm(instance=get_profile())

    context = {
        'profile': get_profile(),
        'profile_form': profile_form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    if request.method == "POST":
        profile_form = DeleteProfileForm(request.POST, instance=get_profile())
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home page')
    else:
        profile_form = DeleteProfileForm(instance=get_profile())

    context = {
        'profile': get_profile(),
        'profile_form': profile_form,
    }
    return render(request, 'delete-profile.html', context)
