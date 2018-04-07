from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(requset):
    if requset.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=requset.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = requset.user
            new_item.save()
            messages.success(requset, 'Image added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmaklet via GET
        form = ImageCreateForm(data=requset.GET)
    return render(requset,
                  'images/image/create.html',
                  {'sections': 'images',
                   'form': form})
