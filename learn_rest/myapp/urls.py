from django.urls import path,include;
from myapp import views;
from rest_framework import routers;
router=routers.DefaultRouter();
router.register(r'languages',views.LanguageView);
router.register(r'programmers',views.ProgrammerView);
router.register(r'Paradigms',views.ParadigmView);
urlpatterns=[
path('',views.home,name="home"),
path('apis/',include(router.urls)),
];
