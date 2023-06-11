from django.shortcuts import render, redirect, HttpResponse
from .models import User, Book
from django.contrib import messages



def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        context = {
            "user": User.objects.get(id=user_id),
            "books": Book.objects.all(),
        }
        return render(request, "dashboard.html", context)
    else:
        return redirect('/logout')


def create_book(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            errors = Book.objects.validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
            else:
                title = request.POST.get('title')
                desc = request.POST.get('desc')
                uploaded_by = User.objects.get(id=user_id)
                Book.objects.create(title=title, desc=desc, uploaded_by=uploaded_by)
            return redirect('/dashboard')
    else:
        return HttpResponse('Method not allowed', status=405)


def show_creator(request, book_id):
    user_id = request.session.get('user_id')
    if user_id:
        context = {
            "user": User.objects.get(id=user_id),
            "this_book": Book.objects.get(id=book_id),
        }
        return render(request, "creator.html", context)
    else:
        return redirect('/logout')


def add_favorite(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        page_type = request.POST.get('the_page_type')
        if user_id:
            book_id = request.POST.get('this_book_id')
            this_user = User.objects.get(id=user_id)
            this_book = Book.objects.get(id=book_id)
            this_book.books.add(this_user)
        if page_type == "creator_page":
            return redirect('/dashboard/this_book/' + str(book_id))
        elif page_type == "dashboard_page":
            return redirect('/dashboard')
    else:
        return HttpResponse('Method not allowed', status=405)


def remove_favorites(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        page_type = request.POST.get('the_page_type')
        if user_id:
            book_id = request.POST.get('this_book_id')
            this_user = User.objects.get(id=user_id)
            this_book = Book.objects.get(id=book_id)
            this_book.books.remove(this_user)
        if page_type == "creator_page":
            return redirect('/dashboard/this_book/' + str(book_id))
        elif page_type == "dashboard_page":
            return redirect('/dashboard')
    else:
        return HttpResponse('Method not allowed', status=405)


def update_book(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            book_id = request.POST.get('the_book_id')
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            this_book = Book.objects.get(id=book_id)
            this_book.title = title
            this_book.desc = desc
            this_book.save()
            messages.success(request, 'Book information updated successfully.')
            return redirect('/dashboard/this_book/' + str(book_id))
        else:
            return HttpResponse('Method not allowed', status=405)
    else:
        return redirect('/logout')


def delete_book(request):
    pass
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            book_id = request.POST.get('the_book_id')
            this_book = Book.objects.get(id=book_id)
            this_book.delete()
            messages.success(request, f'The Book {{{this_book.title}}} deleted successfully.')
            return redirect('/dashboard')
        else:
            return HttpResponse('Method not allowed', status=405)
    else:
        return redirect('/logout')