from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project, Reward

from django.views.generic import View

from .forms import CartAddReward
from .cart import Cart

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Agregar(View):
	def post(self,request,pk):
		cart = Cart(request)
		r = get_object_or_404(Reward,id=pk)
		print(r)
		form = CartAddReward(request.POST)
		print (form)
		if form.is_valid():
			print('is valid')
			cd = form.cleaned_data
			cart.add(product=r,
				quantity=cd['quantity'],
				update_quantity=cd['update'])
		# return redirect('cart:cart_detail')
		print(len(cart))
		return redirect('cart:cart_detail')

class Remove(View):
	def get(self,request,pk):
		cart = Cart(request)
		r = get_object_or_404(Reward,id=pk)
		cart.remove(r)
		return redirect('cart:cart_detail')

class Detalle(View):
	@method_decorator(login_required)
	def get(self,request):
		cart = Cart(request)
		return render(request,'cart/detalle.html',{'cart':cart})
