from django import template
register=template.Library()
@register.filter(name='Swapping')
def Swap(value):
    return value.swapcase()

@register.filter()
def counting(value,arg):
    return value.count(arg)

@register.filter(name='rep')
def remove(value,arg):
    return value.replace(arg,'')



#register.filter('Swapping',Swap)
#register.filter('counting',counting)
#register.filter('remove',remove)