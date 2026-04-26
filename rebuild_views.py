import os

views_content = """from django.shortcuts import render, redirect
from .models import Faculty, Kafedra, Group, Student, Subject, Teacher, Category, Product, Order, OrderItem, ActionLog, Branch
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, KafedraForm, GroupForm, StudentForm, SubjectForm, TeacherForm, CategoryForm, ProductForm, OrderForm, OrderItemForm, BranchForm
from . import services

def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")

def _log_action(request, *, action: str, entity: str, entity_id=None, message: str):
    try:
        ActionLog.objects.create(
            user=request.user if getattr(request, "user", None) and request.user.is_authenticated else None,
            action=action,
            entity=entity,
            entity_id=entity_id,
            message=message[:255],
            ip_address=_client_ip(request),
            user_agent=(request.META.get("HTTP_USER_AGENT") or "")[:255],
        )
    except Exception:
        pass

def login_required_decorator(func):
    return login_required(func, login_url='login_page')

@login_required_decorator
def logout_page(request):
    _log_action(request, action="logout", entity="Auth", message="User logged out")
    logout(request)
    return redirect("login_page")

def login_page(request):
    error = None
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            _log_action(request, action="login", entity="Auth", message="User logged in")
            return redirect("dashboard")
        else:
            error = "Noto'g'ri foydalanuvchi nomi yoki parol"

    return render(request, 'login.html', {'error': error})

@login_required_decorator
def home_page(request):
    total_orders = Order.objects.count()
    revenue = sum(order.total_price for order in Order.objects.all())
    ctx = {
        'counts': {
            'orders': total_orders,
            'revenue': revenue,
            'products': Product.objects.count(),
            'categories': Category.objects.count(),
            'teachers': Teacher.objects.count(),
            'students': Student.objects.count()
        }
    }
    return render(request, 'dashboard.html', ctx)

# FACULTY
@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Faculty", entity_id=saved.id, message=f"Created faculty: {saved.name}")
        return redirect('faculty_list')
    ctx = {"model":model, "form":form}
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Faculty", entity_id=saved.id, message=f"Edited faculty: {saved.name}")
        return redirect('faculty_list')
    ctx = {"model":model, "form":form}
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Faculty", entity_id=pk, message=f"Deleted faculty: {name}")
    return redirect('faculty_list')

@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    ctx = {"faculties": faculties}
    return render(request, 'faculty/list.html', ctx)

# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Kafedra", entity_id=saved.id, message=f"Created kafedra: {saved.name}")
        return redirect('kafedra_list')
    ctx = {"model":model, "form":form}
    return render(request, 'kafedra/form.html', ctx)

@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Kafedra", entity_id=saved.id, message=f"Edited kafedra: {saved.name}")
        return redirect('kafedra_list')
    ctx = {"model":model, "form":form}
    return render(request, 'kafedra/form.html', ctx)

@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Kafedra", entity_id=pk, message=f"Deleted kafedra: {name}")
    return redirect('kafedra_list')

@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    ctx = {"kafedras": kafedras}
    return render(request, 'kafedra/list.html', ctx)

# SUBJECT
@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Subject", entity_id=saved.id, message=f"Created subject: {saved.name}")
        return redirect('subject_list')
    ctx = {"model":model, "form":form}
    return render(request, 'subject/form.html', ctx)

@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Subject", entity_id=saved.id, message=f"Edited subject: {saved.name}")
        return redirect('subject_list')
    ctx = {"model":model, "form":form}
    return render(request, 'subject/form.html', ctx)

@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Subject", entity_id=pk, message=f"Deleted subject: {name}")
    return redirect('subject_list')

@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()
    ctx = {"subjects": subjects}
    return render(request, 'subject/list.html', ctx)

# TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Teacher", entity_id=saved.id, message=f"Created teacher: {saved.first_name}")
        return redirect('teacher_list')
    ctx = {"model":model, "form":form, "subject_count": Subject.objects.count(), "kafedra_count": Kafedra.objects.count()}
    return render(request, 'teacher/form.html', ctx)

@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Teacher", entity_id=saved.id, message=f"Edited teacher: {saved.first_name}")
        return redirect('teacher_list')
    ctx = {"model":model, "form":form, "subject_count": Subject.objects.count(), "kafedra_count": Kafedra.objects.count()}
    return render(request, 'teacher/form.html', ctx)

@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    name = model.first_name
    model.delete()
    _log_action(request, action="delete", entity="Teacher", entity_id=pk, message=f"Deleted teacher: {name}")
    return redirect('teacher_list')

@login_required_decorator
def teacher_list(request):
    teachers = services.get_teacher()
    ctx = {"teachers": teachers}
    return render(request, 'teacher/list.html', ctx)

# GROUP
@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Group", entity_id=saved.id, message=f"Created group: {saved.name}")
        return redirect('group_list')
    ctx = {"model":model, "form":form}
    return render(request, 'group/form.html', ctx)

@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Group", entity_id=saved.id, message=f"Edited group: {saved.name}")
        return redirect('group_list')
    ctx = {"model":model, "form":form}
    return render(request, 'group/form.html', ctx)

@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Group", entity_id=pk, message=f"Deleted group: {name}")
    return redirect('group_list')

@login_required_decorator
def group_list(request):
    groups = services.get_groups()
    ctx = {"groups": groups}
    return render(request, 'group/list.html', ctx)

# STUDENT
@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Student", entity_id=saved.id, message=f"Created student: {saved.first_name}")
        return redirect('student_list')
    ctx = {"model":model, "form":form}
    return render(request, 'student/form.html', ctx)

@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Student", entity_id=saved.id, message=f"Edited student: {saved.first_name}")
        return redirect('student_list')
    ctx = {"model":model, "form":form}
    return render(request, 'student/form.html', ctx)

@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    name = model.first_name
    model.delete()
    _log_action(request, action="delete", entity="Student", entity_id=pk, message=f"Deleted student: {name}")
    return redirect('student_list')

@login_required_decorator
def student_list(request):
    students = services.get_student()
    ctx = {"students": students}
    return render(request, 'student/list.html', ctx)

# CATEGORY
@login_required_decorator
def category_list(request):
    models = Category.objects.all()
    ctx = {"models": models}
    return render(request, 'category/list.html', ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Category", entity_id=saved.id, message=f"Created category: {saved.name}")
        return redirect('category_list')
    ctx = {"model":model, "form":form}
    return render(request, 'category/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Category", entity_id=saved.id, message=f"Edited category: {saved.name}")
        return redirect('category_list')
    ctx = {"model":model, "form":form}
    return render(request, 'category/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Category", entity_id=pk, message=f"Deleted category: {name}")
    return redirect('category_list')

# PRODUCT
def product_list(request):
    categories = Category.objects.prefetch_related('products').all()
    cart_total = request.session.get('cart_total', 0)
    ctx = {"categories": categories, "cart_total": cart_total}
    return render(request, 'index_1.html', ctx)

@login_required_decorator
def product_admin_list(request):
    models = Product.objects.all()
    ctx = {"models": models}
    return render(request, 'product/list.html', ctx)

@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Product", entity_id=saved.id, message=f"Created product: {saved.name}")
        return redirect('product_admin_list')
    ctx = {"model":model, "form":form}
    return render(request, 'product/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Product", entity_id=saved.id, message=f"Edited product: {saved.name}")
        return redirect('product_admin_list')
    ctx = {"model":model, "form":form}
    return render(request, 'product/form.html', ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Product", entity_id=pk, message=f"Deleted product: {name}")
    return redirect('product_admin_list')

# ORDERS
@login_required_decorator
def order_admin_list(request):
    models = Order.objects.all().order_dict('-created_at') if hasattr(Order.objects.all(), 'order_dict') else Order.objects.all().order_by('-created_at')
    ctx = {"models": models}
    return render(request, 'order/list.html', ctx)

@login_required_decorator
def order_detail(request, pk):
    model = Order.objects.get(pk=pk)
    ctx = {"model": model}
    return render(request, 'order/detail.html', ctx)

# ADMIN USERS
@login_required_decorator
def admin_user_list(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    users = User.objects.filter(is_staff=True)
    ctx = {"models": users}
    return render(request, 'admin_users/list.html', ctx)

@login_required_decorator
def admin_user_create(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = User.objects.create_user(username=username, email=email, password=password)
        u.is_staff = True
        u.save()
        _log_action(request, action="create", entity="AdminUser", entity_id=u.id, message=f"Created admin user: {username}")
        return redirect('admin_user_list')
    return render(request, 'admin_users/form.html')

@login_required_decorator
def admin_user_password(request, pk):
    if not request.user.is_superuser:
        return redirect('dashboard')
    u = User.objects.get(pk=pk)
    if request.method == 'POST':
        password = request.POST.get('password')
        u.set_password(password)
        u.save()
        _log_action(request, action="edit", entity="AdminUser", entity_id=u.id, message=f"Changed password for user: {u.username}")
        return redirect('admin_user_list')
    return render(request, 'admin_users/password.html', {'model': u})

@login_required_decorator
def admin_user_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('dashboard')
    u = User.objects.get(pk=pk)
    username = u.username
    u.delete()
    _log_action(request, action="delete", entity="AdminUser", entity_id=pk, message=f"Deleted admin user: {username}")
    return redirect('admin_user_list')

# BRANCH
@login_required_decorator
def branch_list(request):
    models = Branch.objects.all()
    ctx = {"models": models}
    return render(request, 'branch/list.html', ctx)

@login_required_decorator
def branch_create(request):
    model = Branch()
    form = BranchForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="create", entity="Branch", entity_id=saved.id, message=f"Created branch: {saved.name}")
        return redirect('branch_list')
    ctx = {"model":model, "form":form}
    return render(request, 'branch/form.html', ctx)

@login_required_decorator
def branch_edit(request, pk):
    model = Branch.objects.get(pk=pk)
    form = BranchForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        saved = form.save()
        _log_action(request, action="edit", entity="Branch", entity_id=saved.id, message=f"Edited branch: {saved.name}")
        return redirect('branch_list')
    ctx = {"model":model, "form":form}
    return render(request, 'branch/form.html', ctx)

@login_required_decorator
def branch_delete(request, pk):
    model = Branch.objects.get(pk=pk)
    name = model.name
    model.delete()
    _log_action(request, action="delete", entity="Branch", entity_id=pk, message=f"Deleted branch: {name}")
    return redirect('branch_list')

def filiallar_page(request):
    branches = Branch.objects.all()
    cart_total = request.session.get('cart_total', 0)
    ctx = {
        "branches": branches,
        "cart_total": cart_total
    }
    return render(request, 'filiallar.html', ctx)
"""

with open("C:/Users/Asus/.gemini/antigravity/scratch/maxway/adminapp/views.py", "w", encoding="utf-8") as f:
    f.write(views_content)
