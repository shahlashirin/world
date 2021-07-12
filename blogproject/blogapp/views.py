from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import blog
from.forms import ModeForm

# Create your views here.
def fun(request):
  obj= blog.objects.all()
  return render(request, "index.html", {'results': obj})


# def addition(request):
#     num1 = int(request.POST["num1"])
#     num2 = int(request.POST["num2"])
#     num3 = num1+num2
#     return render(request,"result.html",{"add":num3})

def detail(request,blog_id):
    obj1 = blog.objects.get(id=blog_id)
    return render(request,"detail.html",{'results':obj1})

def add_blog(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        image=request.FILES['image']
        b=blog(name=name,desc=desc,image=image)
        b.save()
        print("blog added")
    return render(request,"add_blog.html")

def update(request,id):
    obj2 = blog.objects.get(id=id)
    form = ModeForm(request.POST or None, request.FILES,instance=obj2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'obj2':obj2})

def delete(request,id):
    if request.method=="POST":
      obj=blog.objects.get(id=id)
      obj.delete()
      return redirect('/')
    return render(request,'delete.html')
