from django import template
from main.forms import RidesearchForm 
register = template.Library()
import pdb
@register.simple_tag
def searchform(*args):
    #pdb.set_trace()    
    return RidesearchForm()
    