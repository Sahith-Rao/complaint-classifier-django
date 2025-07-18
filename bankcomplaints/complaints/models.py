from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('retail_banking', 'Retail Banking'),
        ('credit_reporting', 'Credit Reporting'),
        ('mortgages_and_loans', 'Mortgages and Loans'),
        ('debt_collection', 'Debt Collection'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}" 