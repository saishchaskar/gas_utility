from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('id', 'user', 'request_type', 'details_short', 'status')

    # Customize the way 'details' are displayed by truncating it for readability
    def details_short(self, obj):
        """Truncate the details field for display in the list view."""
        return obj.details[:50] + '...' if len(obj.details) > 50 else obj.details
    details_short.short_description = 'Details'  # This is the label displayed in the admin list

    # Optionally, you can add a search bar to search by username or details
    search_fields = ('user__username', 'details')

    # Optional: Add filters to the sidebar (e.g., by request_type or status)
    list_filter = ('request_type', 'status','user')

    # Default ordering to show the most recent requests first
    ordering = ('-submitted_at',)  # Order by the most recent submission

    readonly_fields = ('user', 'request_type', 'details', 'attachment', 'submitted_at')

    # Define admin action to send email notification based on status
    def send_status_email(self, request, queryset):
        """Send email to the user based on the status of the request."""
        for obj in queryset:
            # Subject and message template
            subject = f"Your Service Request Status: {obj.get_status_display()}"
            message = f"Dear {obj.user.username},\n\nYour service request with ID {obj.id} has been updated to the status: {obj.get_status_display()}.\n\n For the Below Details \n\n Details: {obj.details}\n\nThank you."
            
            # The email will be sent to the user's email address linked in the User model
            recipient_list = [obj.user.email]

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,  # Sender's email (from settings)
                    recipient_list
                )
            except Exception as e:
                # If there is an error, notify the admin user
                self.message_user(request, f"Failed to send email to {obj.user.username}: {e}", level='error')
            else:
                # Success message in the admin interface
                self.message_user(request, f"Email sent to {obj.user.username} about the status update.", level='success')

    send_status_email.short_description = "Send email to user about status update"

    # Add the action to the admin panel
    actions = [send_status_email]

    # Optional: You can also define the behavior when an admin changes the status
    def save_model(self, request, obj, form, change):
        """Override save model to trigger email on status change."""
        if change and obj.status != form.initial['status']:
            # Only send email when the status has changed
            self.send_status_email(request, [obj])
        super().save_model(request, obj, form, change)
