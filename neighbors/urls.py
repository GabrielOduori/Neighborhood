from django.conf.urls import url
from neighbors import views as neighbors_views
# from projects import views as project_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', neighbors_views.home, name = 'home'),
    url(r'^neighborhoods/$', neighbors_views.neighborhoods, name = 'neighborhoods'),
    url(r'^neighborhood/(?P<id>\d+)/$', neighbors_views.neighborhood_detail, name = 'neighborhoods'),
          
      
      
    # url(r'^checkin/$', neighbors_views.checkin, name = 'checkin'),
    # url(r'^neighbor/location$', neighbors_views.locations, name = 'checkin'),
    # url(r'^api/profile/$', project_views.ProfileAPI.as_view()),
    # url(r'^api/project/$', project_views.ProjectAPI.as_view()),
   
      
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

