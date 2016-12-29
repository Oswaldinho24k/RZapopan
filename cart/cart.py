from decimal import Decimal
from django.conf import settings
from projects.models import Reward as Product


class Cart(object):
	def __init__(self,request):
		"""
		Inicializamos el carrito de compras
		"""
		self.session = request.session
		self.cart = self.session.get(settings.CART_SESSION_ID)
		if not self.cart:
			#Guardar el carrito vacio en la session
			self.cart = self.session[settings.CART_SESSION_ID] = {}

	def add(self, product, quantity=1, update_quantity=False):
		"""
		Agregamos un producto nuevo al carrito o lo actualizamos
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {
				'quantity':0,
				'price':str(product.price)
			}
			
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			# cambio esto para evitar sumas "+="
			self.cart[product_id]['quantity'] = quantity
		self.save()
	def save(self):
		#Actualizamos el carrito en la session
		self.session[settings.CART_SESSION_ID] = self.cart
		#marcamos la session como modificada para asegurarnos que si guardamos
		self.session.modified = True

	def remove(self,product):
		"""
		Eliminamos un producto del carrito
		"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		"""
		Iterar en los elementos del carrito y traer
		 los productos de la base de datos
		"""
		product_ids = self.cart.keys()
		#traer el producto y agregarlo
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		"""
		Cuenta todos los items en el carrito
		"""
		return sum(item['quantity'] for item in self.cart.values())

		"""
		suma = 0
		for item in self.cart.values():
			suma = sum(item['quantity'])
		return suma
		"""

	def get_total_price(self):
		return sum(Decimal( item['price']) * item['quantity'] for item in self.cart.values() )


	def clear(self):
		#borrar el carrita de las esion de usuario
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True