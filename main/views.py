from django.shortcuts import render, redirect
from . forms import JobForm

# Create your views here.
def home(request):
    return render(request=request,
    template_name='main/home.html')


def new_work(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = JobForm()

    return render(
        request=request,
        template_name = 'main/home.html',
        context = {
            'object': "Job",
            "form": form
            }
        )