from hashlib import new
from django.shortcuts import redirect, render
from store.models import Customer, customer
from store.models.room import Room
from store.models.message import Message
from django.http import HttpResponse, JsonResponse

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'roomchat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    customer_id = request.session.get('customer')
    customer = Customer.get_customer_by_id(customer_id)
    room = customer.mess_code
    username = customer.last_name

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})