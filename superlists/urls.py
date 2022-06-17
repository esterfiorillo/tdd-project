from lists import views

urlpatterns = [
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
]