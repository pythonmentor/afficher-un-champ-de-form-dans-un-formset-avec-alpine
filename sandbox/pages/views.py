from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.forms import formset_factory

from .forms import CreateTask, CreateTaskHelper


class HomeView(TemplateView):
    template_name = "pages/home.html"


home_view = HomeView.as_view()


def hx_display_task_formset(request):
    return TemplateResponse(
        request,
        "pages/home.html#task_formset",
        {
            "formset": formset_factory(CreateTask, extra=2),
            "helper": CreateTaskHelper(),
        },
    )
