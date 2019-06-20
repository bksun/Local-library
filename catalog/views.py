from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


class BookListView(generic.ListView):
    """Generic class-based detail view for a book."""
    model = Book
    paginate_by = 2


class AuthorListView(generic.ListView):
    """Generic class-based detail view for a book."""
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Author


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
