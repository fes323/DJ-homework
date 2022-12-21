from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_Counter = 0
        for form in self.forms:
            form_dict = form.cleaned_data
            data = form_dict.get('is_main')
            if data == True:
                is_main_Counter += 1
                print(is_main_Counter)
            if is_main_Counter > 1:
                raise ValidationError('ВНИМАНИЕ: основной тег может быть только один! Отметьте галочкой только 1 тег.')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 5


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    display_list = ['id']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    display_list = ['id']

