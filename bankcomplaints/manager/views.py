from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from complaints.models import Complaint

@staff_member_required
def manager_complaints_view(request):
    selected_category = request.GET.get('category', '')
    categories = Complaint.CATEGORY_CHOICES
    if selected_category:
        complaints = Complaint.objects.filter(category=selected_category).order_by('-created_at')
    else:
        complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'manager/manager_complaints.html', {
        'complaints': complaints,
        'categories': categories,
        'selected_category': selected_category,
    })