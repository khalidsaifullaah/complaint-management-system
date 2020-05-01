from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Employee 
# Create your models here.
class Complaint(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Enter your complaint')
    details = models.TextField(verbose_name= 'Explain in more detail')
    date_posted = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    status_choices = [
        (1, 'Pending'),
        (2, 'Solved')
    ]
    status = models.IntegerField(choices=status_choices, default=1)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('complaint-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=120)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.complaint.title, str(self.user.username))