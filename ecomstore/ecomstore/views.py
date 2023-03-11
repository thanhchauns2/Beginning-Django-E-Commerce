from django.shortcuts import render
from django.template import RequestContext

def file_not_found_404(request, *args, **argv):
    page_title = 'Page Not Found'
    return render(request, '404.html', locals())

def file_not_found_500(request, *args, **argv):
    page_title = 'Page Not Found'
    return render(request, '500.html', locals())