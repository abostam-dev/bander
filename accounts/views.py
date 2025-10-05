from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm


# تسجيل حساب جديد
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول بعد الإنشاء مباشرة
            messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
            return redirect("home")  # يوجه للصفحة الرئيسية
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✅")
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج")
    return redirect("home")
