from django.db import models
from commerce.models import Order


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="الطلب")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    status = models.CharField(max_length=50, default="غير مدفوع", verbose_name="الحالة")
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="رقم العملية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "دفعة"
        verbose_name_plural = "المدفوعات"

    def __str__(self):
        return f"دفعة {self.id} - {self.status}"


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التقرير")
    report_type = models.CharField(max_length=100, verbose_name="نوع التقرير")
    details = models.TextField(blank=True, null=True, verbose_name="التفاصيل")

    class Meta:
        verbose_name = "تقرير"
        verbose_name_plural = "التقارير"

    def __str__(self):
        return f"{self.report_type}"
