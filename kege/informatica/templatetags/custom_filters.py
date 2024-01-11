from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter(name='get_item_table')
def get_item_table(dictionary, key, item):
    answer_table = dictionary.get(key, '')
    return answer_table[item]
