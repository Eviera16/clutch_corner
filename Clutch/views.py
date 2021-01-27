from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .form import ImageForm

def login(request):
    return render(request, "login.html")

def loginuser(request):
    errors = User.objects.logValidator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    
    if request.POST['user_name'] == "adminUser":
        request.session['loginID'] = "admin"
    else:
        new_user = User.objects.create(username=request.POST['user_name'], password=request.POST['password'])
        request.session['loginID'] = new_user.id
    return redirect('/index')

def index(request):


    allItems = Items.objects.all()
    allImages = Image.objects.all()

    item = Items.objects.get(id=1)

    logged = request.session['loginID']
    admin = "admin"

    print("logged here")
    print(logged)
    print("admin here")
    print(admin)

    context = {
        "allItems" : allItems,
        "allImages" : allImages,
        "item" : item,
        "logged" : logged,
        "admin" : admin
    }

    return render(request, "index.html", context)

def addItem(request):
    if request.method == "POST":
        print("it is a post request")
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            newItem = Items.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                price=request.POST['price'],
                imgNums = [obj.id]
            )
            newItem.save()
        
        return redirect('/')
    else:
        form=ImageForm() 

        context = {
            "form" : form
        }
    return render(request, "addItem.html", context)

def itemInfo(request, id):

    item = Items.objects.get(id=id)

    print(item)
    print(item.title)
    print(item.description)
    print(item.price)

    imgNumslen = len(item.imgNums)

    print(item.imgNums)

    imgNumArr = item.imgNums

    print("here now")
    print(imgNumslen)

    admin = "admin"

    allPics = Image.objects.all()

    logged = request.session['loginID']

    context = {
        "item" : item,
        "allPics" : allPics,
        "imgNumslen" : imgNumslen,
        "imgNumArr" : imgNumArr,
        "logged" : logged,
        "admin" : admin
    }

    return render(request, "itemInfo.html", context)

def editItem(request, id):
    if request.method == "POST":
        print("it is a post request")
        item = Items.objects.get(id=id)
        allImages = Image.objects.all()
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            item.imgNums += [obj.id]
            item.save()
        
        return redirect('/index')
    else:
        form=ImageForm() 
        item = Items.objects.get(id=id)
        allImages = Image.objects.all()

        numArr = item.imgNums
        indexArr = []
        ind = 1

        for i in numArr:
            if i != None:
                indexArr.append(ind)
                ind += 1

        indLen = len(indexArr)


        arrLen = indLen // 2
        lenArr = []

        # item.imgNums.insert(1, item.imgNums.pop(5))
        # item.save()
        print("new list here: ")
        print(item.imgNums)

        for i in range(2):
            lenArr.append(i)

        context = {
            "form" : form,
            "item" : item,
            "allImages" : allImages,
            "indexArr" : indexArr,
            "lenArr" : lenArr
        }

    return render(request, "editItem.html", context)

def addImage(request, id):
    if request.method == "POST":
        print("it is a post request")
        item = Items.objects.get(id=id)
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            item.imgNums += obj.id
            item.save()
        return redirect('/editItem/${id}')


def gallery(request):
    return render(request, "gallery.html")

