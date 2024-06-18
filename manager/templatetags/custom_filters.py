from django import template

register = template.Library()

@register.filter
def format_phone(value):
    try:
        phone_number = ''.join(filter(str.isdigit, value))
        
        formatted_phone = f'+7 ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}'
        
        return formatted_phone
    except:
        return value