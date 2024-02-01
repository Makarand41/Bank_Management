from django.urls import path
from .views import *

urlpatterns = [

    path('',homef),
    path("viewAllUP/", viewAllf),
    path("addUP/", addf),
    path("deleteUP/<int:user_id>", deletef),


    path('updateUP/<int:user_id>/', update_userf),
    path('do-update-userUP/<int:user_id>/', do_update_userf),



path("depositeUP/", depositf),
path("withdrawUP/", withdrawf),
    path("transferUP/", transferf),
path("viewoneUP/", viewonef),
]
