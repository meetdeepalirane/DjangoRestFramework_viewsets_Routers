from book_app.api.viewsets import BookViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register('book_app',BookViewSet,basename="book")
# for url in router.urls:
#     print(url, '\n')