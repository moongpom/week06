from django.shortcuts import render,redirect,get_object_or_404
from .models import Book

# Create your views here.
def homePage(request):
    books=Book.objects.all()
    return render(request,"homePage.html",{'bookContents':books})

def detailPage(request,bookId):
    books=get_object_or_404(Book,pk=bookId)
    return render(request,"detailPage.html",{'bookContents':books})

def newPage(request):
    return render(request,"newPage.html")

def create(request):
    createBook=Book()
    createBook.image=request.FILES['image']
    createBook.title=request.POST['title']
    createBook.writer=request.POST['writer']
    createBook.body=request.POST['body']
    createBook.publisher=request.POST['publisher']
    createBook.pub_date=request.POST['pub_date']
    createBook.save()
    return redirect("detailBook",createBook.id)

def edit(request,bookId):
    editBook=Book.objects.get(id=bookId)
    return render(request,'editPage.html',{'bookContents':editBook})

def update(request,bookId):
    updateBook=Book.objects.get(id=bookId)
    updateBook.title=request.POST['title']
    updateBook.writer=request.POST['writer']
    updateBook.body=request.POST['body']
    updateBook.publisher=request.POST['publisher']
    updateBook.pub_date=request.POST['pub_date']
    updateBook.save()
    return redirect("detailBook",updateBook.id)

def delete(request,bookId):
    deleteBook=Book.objects.get(id=bookId)
    deleteBook.delete()
    return redirect('homePage')
