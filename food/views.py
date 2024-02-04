from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.   
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse("Hello, world. You're at the polls item.")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm()
        
    context = {
        'form': form
    }
    return render(request, 'food/item-form.html', context)


def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm(instance=item)

    context = {
        'form': form
    }
    return render(request, 'food/item-form.html', context)
    
    
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context = {
        'item': item
    }
    return render(request, 'food/item-delete.html', context)
    