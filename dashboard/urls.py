from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add_new', views.create_book),
    path('this_book/<int:book_id>', views.show_creator),
    path('add_favorite', views.add_favorite),
    path('remove_favorites', views.remove_favorites),
    path('update', views.update_book),
    path('delete', views.delete_book),
    # path('<int:id>', views.show_book, name='show_book'),
    # path('update/<int:id>', views.update_book),
    # path('delete/<int:id>', views.delete_book),
]
