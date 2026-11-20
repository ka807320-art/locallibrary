from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Мінімальні маршрути-заглушки для get_absolute_url() з практичної роботи.
    path("catalog/book/<int:pk>/", views.book_detail, name="book-detail"),
    path("catalog/author/<int:pk>/", views.author_detail, name="author-detail"),
    path("catalog/language/<int:pk>/", views.language_detail, name="language-detail"),
]
