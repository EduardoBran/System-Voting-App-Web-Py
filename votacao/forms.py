from django.forms import ModelForm, inlineformset_factory

from .models import *


class PollsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceMetaForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

ChoiceMetaInLineFormset = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceMetaForm,
    extra=3,
)
