from django.db import models
from django.conf import settings
from commerce.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="unpaid")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Report {self.report_type} - {self.created_at.date()}"
