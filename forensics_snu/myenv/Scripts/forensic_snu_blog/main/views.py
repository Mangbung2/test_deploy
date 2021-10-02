from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Write
from .forms import WriteForm

# Create your views here.
def index(request):
    all_write = Write.objects.all()
    paginator = Paginator(all_write, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(
        request,
        'index.html',
        {
            'all_write':all_write,
            'posts':posts,
        },
        )

def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('index') # 글 쓰고 인덱스로 감
    else:
        create_form = WriteForm()
    return render(
        request,
        'create.html',
        {'create_form':create_form}
        )

def update(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    if request.method == 'POST':
        create_form = WriteForm(request.POST, instance=my_write)#기존내용을 수정해야 하니 instance로 받아오기
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    else:
        create_form = WriteForm(instance=my_write)
    return render(
        request,
        'create.html',
        {'create_form':create_form}
    )

def delete(request, write_id):
    my_write = get_object_or_404(Write,id=write_id)
    my_write.delete()
    return redirect('index')

def detail(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)#없는 페이지에 대해 404에러
    return render(
        request,
        'detail.html',
        {'my_write':my_write}
    )