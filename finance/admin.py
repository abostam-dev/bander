from django.contrib import admin
from .models import Payment, Report

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("order__id", "transaction_id")

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "report_type", "created_at")
    list_filter = ("report_type", "created_at")
    search_fields = ("report_type",)
