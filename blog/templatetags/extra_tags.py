from django import template

register = template.Library()

@register.filter
def rating(digit):
    try:
        digit = int(digit/2)
        value = [1 for x in range(digit)]
        for i in range(len(value),5):
            value.append(0)
        return value
    except:
        return [00000]