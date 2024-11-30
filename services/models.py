from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    # Updated STATUS_CHOICES to reflect the sequential timeline
    STATUS_CHOICES = [
        ('S', 'Submitted'),
        ('R', 'Received'),
        ('I', 'In Review'),
        ('C', 'Completed'),
        ('P', 'Pending'),
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
    status = models.CharField(max_length=20, default='S', choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        """Override save method without forward-only status progression."""
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ServiceRequest {self.id} - {self.get_status_display()}"