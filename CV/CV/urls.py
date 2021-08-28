from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path("", RedirectView.as_view(url='/community/', permanent=True)), # 기본주소 입력했을 때, /community로 넘겨줌.
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # 정적파일 처리(이미지, 자바스크립트 등)
