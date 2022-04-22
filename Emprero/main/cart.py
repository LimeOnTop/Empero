from django.conf import settings

from main.models import *


class SessionCart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ClothesSizes.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product.cloth
        for item in self.cart.values():
            item['total_price'] = item['quantity'] * item['price']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'size': str(product.size.name),'quantity': 1, 'price': str(product.cloth.price)}
        # elif size not in self.cart[product_id]:
            # self.cart[product_id]['size'] += ', ' + size
            # self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
