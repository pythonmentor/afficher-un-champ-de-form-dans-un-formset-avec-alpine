from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit


class DateInput(forms.DateInput):
    input_type = "date"


class CreateTask(forms.Form):
    description = forms.CharField(label="Nom:")
    has_date = forms.BooleanField(
        label="A-t-elle une date associée ?",
        widget=forms.CheckboxInput(
            attrs={"@change": "displayDate = !displayDate;"}
        ),
    )
    date = forms.DateField(
        label="Date:",
        widget=DateInput(),
    )


class CreateTaskHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = "post"
        self.disable_csrf = True
        self.layout = Layout(
            Div(
                "description",
                "has_date",
                Div("date", x_show="displayDate"),
                x_data="{ displayDate: false }",
                css_class="formset-form mb-2 p-2",
            )
        )
        self.add_input(Submit("submit", "Créer", css_class="btn btn-danger"))
