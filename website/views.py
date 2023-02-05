from django.shortcuts import redirect
from . import views
#from web.forms import UserImageForm
#from .models import Uploadimg  


def index_redirect(request):
    return redirect('/web/')