from django.urls import path

from . import views
app_name ='blogapp'
urlpatterns =[
    path('',views.fun,name='fun'),
    # path('add',views.addition,name='add'),
    path('blog/<int:blog_id>',views.detail,name='detail'),
    path('add/',views.add_blog,name='add_blog'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]