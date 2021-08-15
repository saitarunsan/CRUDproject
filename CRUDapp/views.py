from django.shortcuts import render, redirect

# Create your views here.
from .models import ClientInfo


def home(request):  # READ

    all_clients = ClientInfo.objects.all()

    context = {
        'all_clients': all_clients,

    }
    return render(request, 'index.html', context)


def add_client(request):  # CREATE

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')

        # print(10*'---',name,email,phone,status)

        client = ClientInfo(name=name, email=email, phone=phone, status=status)
        client.save()
        return redirect('home')

    #return render(request, 'index.html')


def delete_client(request, id):  # DELETE

    client = ClientInfo.objects.get(id=id)
    client.delete()
    return redirect('home')

    r  # eturn render(request,'index.html')


def edit_client(request, id):  # UPDATE
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')

        # print(10*'---',name,email,phone,status)

        client = ClientInfo.objects.get(id=id)

        client.name = name
        client.email = email
        client.phone = phone
        client.status = status
        client.save()

        return redirect('home')

    else:
        client = ClientInfo.objects.get(id=id)
        context = {
            'client': client,
        }
        return render(request, 'edit.html', context)
