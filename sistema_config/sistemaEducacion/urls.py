from django.urls import path
from .views import *
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('sistema_Profe/', sistema_Profe, name='sistema_Profe'),
    path('calificar/', calificar, name='calificar'),    
    path('planificar/', planificar, name='planificar'),
    path('clase/', clase, name='clase'), 
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('apoderado/', apoderado , name= 'apoderado'),
    path('revisar_notas/', revisar_notas , name= 'revisar_notas'),
    path('notificar/', notificar , name= 'notificar'),
    path('admin_apoderado/', admin_ap , name= 'admin_apoderado'),
    path('admin_alum/', admin_al , name= 'admin_alum'),
    path('admin_profe/', admin_pro , name= 'admin_profe'),
    path('admin_user/', admin_user , name= 'admin_user'),
    path('control_plan/', control_plan , name= 'control_plan'),
    path('admin_evento/', admin_evento , name= 'admin_evento'),
<<<<<<< HEAD
    #eliminar
    path('deleteapoderado/<p_run>/',delete_apoderado, name='delete_apoderado'),
    #modificar
    path('admin_apoderadoModi/<str:p_run>/', admin_apoderadoModi, name='admin_apoderadoModi'),
    path('admin_apoderado/modificar/<p_run>/', update_apoderado, name='update_apoderado'),

]
=======
    path('dashboards/', dashboards , name= 'dashboards'),
    path('pagoMatricula/', pagoMatricula , name= 'pagoMatricula'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> df718800e81134f60bb61d4aeacf48d601e5e7d9
