from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def home(request):
    if request.method=='POST':
        new_todo=Todo(title= request.POST['title'])
        print( request.POST['title'])
        print("Done")
        new_todo.save()
        return  redirect('home')

    todo= Todo.objects.all()
    return render(request,'index.html',{'todos':todo})

def delete(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return  redirect('home')
