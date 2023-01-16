
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('departments', DepartmentView )
router.register('personals', PersonalView )

urlpatterns = router.urls
