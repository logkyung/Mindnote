from django.shortcuts import render, redirect
from diary.models import Page
from diary.forms import PageForm

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    context = {"object_list":object_list}
    return render(request, 'diary/page_list.html', context=context)


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
