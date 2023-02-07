from django.shortcuts import render,redirect
from .forms import Sampleform
from .models import Sample
# Create your views here.


def HOME(request):
    return render(request, 'index.html')


def FormView(request):
    success = False
    form = Sampleform()
    error = False
    if request.method == "POST":
        form = Sampleform(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            if len(user.phone) == 10 and str(user.phone).isnumeric():
                user.save()
                return redirect('sucees',user.email)
                
                
            else:
                error = "Phone number error"
                print(error)

        else:
            error = form.errors.as_text
            print(error)

    context = {'form': form, "error": error, "success": success}
    return render(request, 'form.html', context=context)


def Sucess(request, pk):
    result = Sample.objects.get(email=pk)
    print(result)
    context = {"user": result}
    return render(request, 'success.html', context=context)
