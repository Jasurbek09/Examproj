from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class National_team(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='media')
    score = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    goals_difference = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
