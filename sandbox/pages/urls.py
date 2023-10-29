from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home_view, name="home"),
    path(
        "hx/display-task-formset/",
        views.hx_display_task_formset,
        name="hx-display-task-formset",
    ),
]
