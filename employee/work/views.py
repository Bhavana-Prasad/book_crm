from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm,BookForm,DetailForm,MobileForm,StudentsForm
from work.models import Emp,Book,Details,Mobiles,Students

# Create your views here.
class Employee(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=EmpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data) 
            #modelname.objects.create(values)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})

class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
#           print(form.cleaned_data)
#           Book.objects.create(**form.cleaned_data)  => ORM query       
            form.save()
#form.save(): method to add the data into database without using orm query(only for modelform)
            print("created")
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
class Booklist(View):
    def get(self,request):
        qs=Book.objects.all()
        return render(request,"booklist.html",{"data":qs})
class BooksView(View):
    def get(self,request,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"booksid.html",{"data":qs})
class Book_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Book.objects.get(id=id).delete()
        return redirect("book-al")

class DetailView(View):
    def get(self,request):
        form=DetailForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=DetailForm(request.POST)
        if form.is_valid():     
            form.save()
            print("created")
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
class Detaillist(View):
        def get(self,request):
            qs=Details.objects.all()
            return render(request,"details.html",{"data":qs})
class DetailsView(View):
        def get(self,request,**kwargs):
            #id=2   only for mentioned id
    # (**kwargs) provides with flexibility to use keyword arguments in our prgm. Using it as a parameter,
      # we can eventually pass many arguments(requests)
            id=kwargs.get("pk")
            qs=Details.objects.get(id=id)
            return render(request,"detailsid.html",{"data":qs})

class MobileView(View):
    def get(self,request):
        form=MobileForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=MobileForm(request.POST)
        if form.is_valid():     
            form.save()
            print("created")
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
class Moblist(View):
    def get(self,request):
        qs=Mobiles.objects.all()
        return render(request,"mob.html",{"data":qs})

class StudentsView(View):
    def get(self,request):
        form=StudentsForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=StudentsForm(request.POST)
        if form.is_valid():     
            form.save()
            print(form.cleaned_data)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})