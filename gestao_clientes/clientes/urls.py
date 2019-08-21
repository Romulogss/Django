from django.urls import path
from .views import (
    PersonList,
    PersonDetail
)
from .views import persons_new
from .views import persons_update
from .views import persons_delete


urlpatterns = [
    path('list/', PersonList.as_view(), name="person_list"),
    path('person/<int:pk>', PersonDetail.as_view(), name="person_detail"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]