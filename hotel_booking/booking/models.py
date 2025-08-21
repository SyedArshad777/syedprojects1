from django.db import models
class Room(models.Model):
    ROOM_TYPES=[
           ('single','Single'),
           ('double','Double'),
           ('suite','Suite'),
           ('luxery','Luxery'),
    ]
    number=models.CharField(max_length=10,unique=True)
    room_type=models.CharField(max_length=10,choices=ROOM_TYPES)
    price_per_night=models.DecimalField(max_digits=8,decimal_places=2)
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return f"ROOM{self.number}({self.room_type})"
class Booking(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    guest_name=models.CharField(max_length=100)
    guest_email=models.EmailField()
    check_in=models.DateField()
    check_out=models.DateField()
    def __str__(self):
        return f"Booking:{self.guest_name}-Room {self.room.number}"
