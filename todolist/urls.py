from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 스키마 설정
schema_view = get_schema_view(
    openapi.Info(
        title="To-Do List API",  # API 제목
        default_version='v1',  # 버전 정보
        description="이것은 Swagger를 사용한 To-Do List API 문서입니다.",  # API 설명
        terms_of_service="https://www.google.com/policies/terms/",  # 서비스 약관 URL
        contact=openapi.Contact(email="your_email@example.com"),  # 연락처 정보
        license=openapi.License(name="BSD License"),  # 라이선스 정보
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 모든 사용자 접근 가능
)

# URL 패턴 정의
urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin URL
    path('', include('tasks.urls')),  # 앱의 URL을 루트 경로로 포함

    # Swagger 및 ReDoc 경로 추가
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc
    path('schema/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # OpenAPI 스키마 (JSON)
]
