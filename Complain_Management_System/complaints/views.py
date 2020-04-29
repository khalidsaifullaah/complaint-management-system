from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Complaint, Feedback
from .forms import FeedbackForm
from users.models import Employee


@login_required
def complaint_list(request):
    complaint_exists = True
    if request.user.profile.is_employee:
        employee_id = Employee.objects.get(employee=request.user)
        user_complaints = Complaint.objects.filter(
            assigned_employee=employee_id).order_by('-id')

    else:
        user_complaints = Complaint.objects.filter(
            user_id=request.user).order_by('-id')

    if len(user_complaints) == 0:
        complaint_exists = False

    paginator = Paginator(user_complaints, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'complaints': page_obj, 
        'complaint_exists': complaint_exists,
        'page_obj': page_obj,
    }
    print(request.user.first_name is "")
    return render(request, 'index.html', context)


@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, id=pk)
    if request.user.profile.is_employee:
        employee_id = Employee.objects.get(employee=request.user)
        if employee_id != complaint.assigned_employee:
            return HttpResponse('<h1>HTTP 403: Access Denied</h1>', status=403)

    else:
        if request.user != complaint.user_id:
            return HttpResponse('<h1>HTTP 403: Access Denied</h1>', status=403)

    feedbacks = Feedback.objects.filter(complaint=complaint).order_by('id')

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST or None)
        if feedback_form.is_valid():
            content = request.POST.get('content')
            feedback = Feedback.objects.create(
                complaint=complaint, user=request.user, content=content)
            feedback.save()
            return HttpResponseRedirect(complaint.get_absolute_url())

    else:
        feedback_form = FeedbackForm()

    context = {
        'complaint': complaint,
        'feedbacks': feedbacks,
        'feedback_form': feedback_form,
    }
    return render(request, 'complaint_detail.html', context)

@login_required
def status_change(request, pk):
    complaint = get_object_or_404(Complaint, id=pk)
    if request.user.profile.is_employee:
        employee_id = Employee.objects.get(employee=request.user)
        if employee_id != complaint.assigned_employee:
            return HttpResponse('<h1>HTTP 403: Access Denied</h1>', status=403)

    else:
        if request.user != complaint.user_id:
            return HttpResponse('<h1>HTTP 403: Access Denied</h1>', status=403)

    form = request.POST.dict()
    if 'Solved' in form:
        print('Solved')
        complaint.status = 2
        complaint.save()
    if 'Pending' in form:
        print('Pending')
        complaint.status = 1
        complaint.save()
    print()
    return HttpResponseRedirect(complaint.get_absolute_url())

class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model = Complaint
    template_name = 'complaint_create.html'
    fields = ['title', 'details']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaint
    template_name = 'complaint_create.html'
    fields = ['title', 'details']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_id:
            return True
        return False


class ComplaintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Complaint
    template_name = 'complaint_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_id:
            return True
        return False
