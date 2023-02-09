from django.db import models
from datetime import datetime

# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"
    # FAILED = 'l', 'Deadline passed'


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
    # start_date = models.DateTimeField()
    end_date = models.DateTimeField(auto_now_add=False)


    def is_end_date(self):
        return datetime.now() > self.end_date

    def __str__(self):
        return self.name