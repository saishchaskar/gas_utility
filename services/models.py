from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    REQUEST_TYPE_CHOICES = [
        ('Complaint', 'Complaint Request'),
        ('Service', 'Service Request'),
        ('Booking', 'Booking Request'),
        ('Other', 'Other Request'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending', choices=STATUS_CHOICES)



class ServiceRequest1(models.Model):
    STATUS_CHOICES = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    PRIORITY_CHOICES = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, verbose_name='Priority')

