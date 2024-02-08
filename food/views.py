from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView

# Create your views here.   
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list
#     }
#     return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    


def item(request):
    return HttpResponse("Hello, world. You're at the polls item.")


# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item
#     }
#     return render(request, 'food/detail.html', context)


class FoodDetail(DeleteView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'


# def create_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('food:index')
#     else:
#         form = ItemForm()
        
#     context = {
#         'form': form
#     }
#     return render(request, 'food/item-form.html', context)


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
    