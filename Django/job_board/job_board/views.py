from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import JobPosting
# Create your views here.


def index(request):
    # jobs = JobPosting.objects.filter(is_active=True)
    active_postings = JobPosting.objects.all()
    context = {
        "job_posts":active_postings
    }
    return render(request, 'job_board/index.html',context)


def job_detail(request,pk):
    job_posts = get_object_or_404(JobPosting,pk=pk, is_active=True)
    context = {
        'job':job_posts
    }
    return render(request,'job_board/detail.html',context)