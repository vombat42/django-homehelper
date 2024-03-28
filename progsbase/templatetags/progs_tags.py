from django import template
from django.db.models import Count

# import progsbase.views as views
from progsbase.models import Tag, Lang
# from progsbase.utils import menu

register = template.Library()


# @register.simple_tag
# def get_menu():
#     return menu


@register.inclusion_tag('progsbase/list_langs.html')
def show_all_langs(cat_selected=0):
    langs = Lang.objects.all()
    return {'langs': langs}
    # return {'langs': langs, 'lang_selected': lang_selected}


@register.inclusion_tag('progsbase/list_tags.html')
def show_all_tags():
    return {'tags': Tag.objects.annotate(total=Count("tags_of_prog")).filter(total__gt=0)}
