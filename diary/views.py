from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from diary.models import Page
from diary.forms import PageForm

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 8)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:   #만약 쿼리스트링에 'page'가 없어서 None이 설정되었다면
        curr_page_num = 1       # 첫 번째 페이지를 가리키는 1로 바꿔준다.
    page = paginator.page(curr_page_num)
    return render(request, 'diary/page_list.html', {'page':page})


def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    context = {"object":object}
    return render(request, 'diary/page_detail.html', context=context)


def info(request):
    return render(request, 'diary/info.html')


def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid(): 
            new_page = form.save()
            return redirect('page-detail', page_id=new_page.id)
    else:
        form = PageForm()
    return render(request, 'diary/page_form.html', {"form":form})


def page_update(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=object.id)
    else:
        form = PageForm(instance=object)
    return render(request, 'diary/page_form.html', {'form':form})


def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm_delete.html', {'object':object})


def index(request):
    return render(request, 'diary/index.html')
