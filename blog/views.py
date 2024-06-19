from django.shortcuts import render,redirect
from .models import Book,Genre,Writer
from books.models import details,authors;
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'genres':Genre.objects.all()
        }
    return render(request, 'index.html',context,{'title':'Home'})


def booklist(request):
    context = {
        'books': Book.objects.all()
        }
    
    return render(request, 'booklist.html', context)

# def writerlist(request):
#     context = {
#         'writers': Writer.objects.all()
#     }
#     return render(request, 'writerlist.html', context)


# def about(request):
#     return render(request, 'about.html', {'title': 'About'})



def bookdetail(request, id):
    
     book= details.objects.get(id=id)
     writer=book.writer_id
     print("Book:", book.writer_id.id)  # Debug statement
     print("Writer:", writer.id) 
    #  print("Writer object:", writer)
     return render(request, 'bookdetails.html',{'book': book,'writer':writer})


def writerdetail(request, id):
    
    writer = authors.objects.get(id=id)
                 
    return render(request, 'authors.html',{'writer': writer})


@login_required
def comments(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username= request.user
            comment.book = book
            comment.save()
            return redirect('bookdetails.html', id=book.id)
            
        
    else:
          form = CommentForm()

    return render(request, 'comments.html', {'form': form})


# def Genres(request, id):
#     genres = Genre.objects.get(id=id)
#     return render(request, 'genrebooklist.html',{'genre': genres})

# def search(request):
#     text_search = request.GET.get("in")
#     booklist= Book.objects.filter(title__icontains= text_search)
#     writerlist=Writer.objects.filter(name__icontains=text_search)
#     return render(request,'search.html',{'booklist':booklist ,'writerlist':writerlist})


# def contact(request):
#      return render(request, 'contact.html', {'title': 'Gallery'})







        



