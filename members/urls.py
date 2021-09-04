from django.urls import path
from .views import CreateUserView, EditUserView, PasswordsChangeView, CreateRepView, DisplayRepView, EditRepView,\
    CreateSupplierView, DisplaySupplierView, EditSupplierView
from . import views
urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('settings/', EditUserView.as_view(), name='settings'),

    path('create_rep/', CreateRepView.as_view(), name='create_rep'),
    path('<int:pk>/rep/', DisplayRepView.as_view(), name='show_rep_profile'),
    path('<int:pk>/edit_rep/', EditRepView.as_view(), name='edit_rep_profile'),

    path('create_supplier/', CreateSupplierView.as_view(), name='create_supplier'),
    path('<int:pk>/supplier/', DisplaySupplierView.as_view(), name='show_supplier'),
    path('<int:pk>/edit_supplier/', EditSupplierView.as_view(), name='edit_supplier'),

]
