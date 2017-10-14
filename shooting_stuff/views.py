from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math
from .models import User

def index(request):
    User.objects.all().delete()
    if request.POST.get('save_name'):
        last_user = User.objects.all().last()
        if last_user is None:
            id = 0
        else:
            id = 1 + last_user.get_ID()

        this_user = User(ID = id, Name = request.POST.get("Name"))
        this_user.save()
        return HttpResponseRedirect('Player' + str(id))
    return render(request, 'index.html', {})

def shoot(request, user_id):

    if request.POST.get("shoot"):
        this_user = User.objects.get(ID=user_id)
        x_value = this_user.get_x()
        y_value = this_user.get_y()
        direction = this_user.get_direction()
        for user in User.objects.exclude(ID=request.POST.get("ID")):
            new_user = User.objects.get(ID = user.get_ID())
            this_x = new_user.get_x()
            this_y = new_user.get_y()
            try:
                if math.atan((this_y - y_value)/(this_x - x_value)) == direction:
                    new_user.kill()
            except:
                pass
        return HttpResponseRedirect('Player' + str(user_id))
    return render(request, 'shoot.html', {})