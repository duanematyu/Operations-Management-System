from django.shortcuts import render

# Create your views here.
def login_page(request):
    # if request == POST:
    #     if form.is_valid():
    #         form.save
    return render(request, "login.html", {})