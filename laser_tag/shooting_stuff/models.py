from django.db import models
class User(models.Model):
    Name = models.CharField(max_length=30)
    ID = models.IntegerField(default = 0)
    X = models.IntegerField(default = 0)
    Y = models.IntegerField(default = 0)
    Direction = models.DecimalField(default = 0)
    Alive = models.BooleanField(default = True)
    def get_x(self):
        return self.X
    def get_y(self):
        return self.Y
    def get_ID(self):
        return self.ID
    def get_direction(self):
        return self.Direction
    def get_name(self):
        return self.Name
    def check_life(self):
        return self.Alive
    def set_x(self):
        return self.X
    def set_y(self):
        return self.Y
    def set_direction(self):
        return self.Direction
    def set_name(self):
        return self.Name
    def kill(self):
        self.Alive = False
# Create your models here.
