from django.shortcuts import render, redirect, get_object_or_404
from .models import Client

def index(request):
    clients = Client.objects.all()   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        Client.objects.create(name=name, email=email, phone=number)
        return redirect("index")
    
    return render(request, 'index.html', {'clients': clients})

def update_client(request, client_id):
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=client_id)
        client.name = request.POST.get('name')
        client.phone = request.POST.get('number')
        client.email = request.POST.get('email')
        client.save()
    return redirect('index')

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('index')


#def ajax_form_submit(request):
 #   if request.is_ajax():
  #      name = request.POST.get('name')
   #     email = request.POST.get('email')
    #    number = request.POST.get('number')
     #   Client.objects.create(name=name, email=email, phone=number)
      #  clients = Client.objects.all()   
       # return HttpResponse(headers={'clients':clients})
       




    



 