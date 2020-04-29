from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Employee


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # profile = Profile.objects.get(user=instance)
        # if profile.is_employee:
        #     Employee.objects.create(employee=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    # profile = Profile.objects.get(user=instance)
    # if profile.is_employee:
    #     Employee.objects.create(employee=instance)


# @receiver(post_save, sender=Profile)
# def create_employee(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_employee:
#             print('created')
#             Employee.objects.create(employee=instance.user)
    



@receiver(post_save, sender=Profile)
def save_employee(sender, instance, **kwargs):

    if Employee.objects.filter(employee = instance.user).exists():
        if not instance.is_employee:
            Employee.objects.filter(employee = instance.user).delete()
    else:
        if instance.is_employee:
            Employee.objects.create(employee=instance.user)
    

 