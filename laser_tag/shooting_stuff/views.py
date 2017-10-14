from django.shortcuts import render
from
import math
from .models import User

def index(request):
    this_user = User(ID = request.get_ID)

def shoot(request):
    this_user = User.objects.get(ID=request.get_ID)
    x_value = this_user.get_x()
    y_value = this_user.get_y()
    direction = this_user.get_direction()
    for user in User.objects.exclude(ID=request.get_ID):
        new_user = User.objects.get(ID = user.get_ID)
        this_x = new_user.get_x()
        this_y = new_user.get_y()
        if math.atan((this_y - y_value)/(this_x - x_value)) == direction:
            new_user.kill()
