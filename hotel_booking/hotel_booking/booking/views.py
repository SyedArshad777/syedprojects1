from django.shortcuts import render,redirect
from .models import Room, Booking
from django.contrib import messages

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/room_list.html', {'rooms': rooms})
def book_room(request,room_id):
    room=Room.objects.get(id=room_id)
    if request.method =='POST':
        guest_name=request.POST['guest_name']
        guest_email=request.POST['guest_email']
        check_in=request.POST['check_in']
        check_out=request.POST['check_out']
        Booking.objects.create(
            room=room,
            guest_name=guest_name,
            guest_email=guest_email,
            check_in=check_in,
            check_out=check_out
        )
        room.is_available=False
        room.save()
        messages.success(request,'room booked successfully!')
        return redirect('room_list')
    return render(request,'booking/book_room.html',{'room':room})
