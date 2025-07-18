from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from complaints.models import Complaint

@staff_member_required  # Only staff (manager) can access
def manager_complaints_view(request):
    # Get all complaints, ordered by category
    complaints_by_category = {}
    categories = [c[0] for c in Complaint.CATEGORY_CHOICES]
    for cat in categories:
        complaints_by_category[cat] = Complaint.objects.filter(category=cat).order_by('-created_at')
    return render(request, 'manager/manager_complaints.html', {
        'complaints_by_category': complaints_by_category,
        'category_labels': dict(Complaint.CATEGORY_CHOICES),
    }) 