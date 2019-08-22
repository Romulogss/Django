from django.urls import path
from .views import (
    PersonList,
    PersonDetail,
    PersonCreate,
    PersonUpdate,
    PersonDelete,
)

urlpatterns = [
    path('list/', PersonList.as_view(), name="person_list"),
    path('new/', PersonCreate.as_view(), name="person_new"),
    path('person/<int:pk>', PersonDetail.as_view(), name="person_detail"),
    path('update/<int:pk>/', PersonUpdate.as_view(), name="persons_update"),
    path('delete/<int:pk>/', PersonDelete.as_view(), name="persons_delete"),
]
