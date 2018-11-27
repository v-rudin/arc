from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from .models import DiadocDocument
from .forms import DiadocDocumentForm
# from news.forms import ArticleForm

import requests

# Create your views here.

class SettingsVariables:
    PAGE_COUNT_IN_PAGINATION = 2

def index(request):
    url = 'https://diadoc-api-test.kontur.ru/Authenticate?login=test&password=test'
    #params = '?login=user@skbkontur.ru&password=qwerty',



    req = requests.post(url, headers=headers)
    print('------------------------')
    print(req.text)
    print('!!!!!!!!!!!!!!!!!!!!!!!!')
   # print(req.text)

    return render(request, 'e_archive/test2.html')

def show_main_page(request):
    return render(request, 'e_archive/test2.html')


def show_records(request):
    # diadoc_document = DiadocDocument()
    paginate_by = SettingsVariables.PAGE_COUNT_IN_PAGINATION
    text1 = request.POST.get('text1')
    list2 = request.POST.get('list2')
    list3 = request.POST.get('list3')
    text4 = request.POST.get('text4')
    text5 = request.POST.get('text5')
    page_number = request.POST.get('page_num')
    if text5 == 'None':
        text5 = ''

    try:
        object_list = DiadocDocument.objects.filter(doc_description__contains=text5)
    except:
        object_list = DiadocDocument.objects.all()
    # object_list = DiadocDocument.objects.filter(doc_description__contains=text5)

    # list = Blog.objects.all()
    if page_number:
        page = page_number
    else:
        page = 1
    paginator = Paginator(object_list, paginate_by)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    # return render(request, 'app/blog_list.html', {'blog_list': blog_list})
    is_paginated = False
    if paginator.num_pages > 1:
        is_paginated = True
    if request.is_ajax():
        html_template = 'e_archive/content.html'
    else:
        html_template = 'e_archive/base_template.html'



    return render(request, html_template, {'object_list': object_list, 'is_paginated': is_paginated, 'text5': text5})
    # http.HttpResponse(json.dumps({'score': 10}))



