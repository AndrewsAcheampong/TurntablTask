from EShop.viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customer', CustomerViewset)

routerA = DefaultRouter()
router.register('product', ProductViewset)

routerB = DefaultRouter()
router.register('order_item', Order_itemViewset)

routerC = DefaultRouter()
router.register('orders', OrderViewset)