from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # Homepg
    path("",views.index,name="home"),

    # Student
    path("enquiry/", views.enquiry, name="enquiry"),
    path('enroll/<int:id>',views.enroll,name ="enroll"),
    path('stdlogin/',views.stdlogin, name = "stdlogin"),
    path('upgrade/<str:department>/<str:email>',views.upgrade),
    path('add_course/<int:id>/<str:email>',views.add_course),
    # courses based on dept
    path('Civil',views.civil,name = "civil"),
    path('Mechanical',views.mechanical),
    path('IT/',views.it,name ="it"),

    # Admin
    path('host/',views.host),
    path('home/',views.admin_result,name = "admin_result"),
    # modifycourses
    path('createcourse/',views.createcourse,name="createcourse"),
    path('edit/<int:id>', views.edit),  
    path('delete/<int:id>/<str:department>', views.destroy),
    # modifytrainer 
    path('addtrainer/',views.addtrainer,name = "addtrainer"),
    path('trainers/',views.trainers,name ="trainers"),
    path('traineredit/<int:id>',views.traineredit),
    path('tdelete/<int:id>',views.tdelete),
    # Enquiries
    path('enquiries/',views.enquiries),
    path('allenq/',views.allenq),
    path('todays_enq/',views.todays_enq),
    # Todo
    path('todo/',views.todo,name = "todo"),
    path('todolist/',views.todolist,name = "todolist"),
    path('todoedit/<int:id>',views.todoedit),
    path('tododelete/<int:id>',views.tododelete),

    # Trainers
    path('trainers_login',views.trainers_login),

    
]
