from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Part

class IndexView(generic.ListView):
	template_name = 'parts/index.html'
	context_object_name = 'in_stock_parts'

	def get_queryset(self):
		"""Shows in stock parts"""
		return Part.objects.filter(inventory__gt=0).order_by('inventory')

class AIView(generic.ListView):
	model = Part
	template_name = 'parts/AI.html'
	context_object_name = 'AI_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='AI').filter(inventory__gt=0)

class BKView(generic.ListView):
	model = Part
	template_name = 'parts/BK.html'
	context_object_name = 'BK_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='BK').filter(inventory__gt=0)

class CLView(generic.ListView):
	model = Part
	template_name = 'parts/CL.html'
	context_object_name = 'CL_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='CL').filter(inventory__gt=0)

class DTView(generic.ListView):
	model = Part
	template_name = 'parts/DT.html'
	context_object_name = 'DT_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='DT').filter(inventory__gt=0)

class ECView(generic.ListView):
	model = Part
	template_name = 'parts/EC.html'
	context_object_name = 'EC_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='EC').filter(inventory__gt=0)

class EGView(generic.ListView):
	model = Part
	template_name = 'parts/EG.html'
	context_object_name = 'EG_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='EG').filter(inventory__gt=0)

class EXView(generic.ListView):
	model = Part
	template_name = 'parts/EX.html'
	context_object_name = 'EX_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='EX').filter(inventory__gt=0)

class FCView(generic.ListView):
	model = Part
	template_name = 'parts/FC.html'
	context_object_name = 'FC_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='FC').filter(inventory__gt=0)

class GHView(generic.ListView):
	model = Part
	template_name = 'parts/GH.html'
	context_object_name = 'GH_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='GH').filter(inventory__gt=0)

class IGView(generic.ListView):
	model = Part
	template_name = 'parts/IG.html'
	context_object_name = 'IG_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='IG').filter(inventory__gt=0)

class ICView(generic.ListView):
	model = Part
	template_name = 'parts/IC.html'
	context_object_name = 'IC_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='IC').filter(inventory__gt=0)

class ITView(generic.ListView):
	model = Part
	template_name = 'parts/IT.html'
	context_object_name = 'IT_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='IT').filter(inventory__gt=0)

class SLView(generic.ListView):
	model = Part
	template_name = 'parts/SL.html'
	context_object_name = 'SL_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='SL').filter(inventory__gt=0)

class SFView(generic.ListView):
	model = Part
	template_name = 'parts/SF.html'
	context_object_name = 'SF_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='SF').filter(inventory__gt=0)

class SPView(generic.ListView):
	model = Part
	template_name = 'parts/SP.html'
	context_object_name = 'SP_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='SP').filter(inventory__gt=0)

class TKView(generic.ListView):
	model = Part
	template_name = 'parts/TK.html'
	context_object_name = 'TK_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='TK').filter(inventory__gt=0)

class WGView(generic.ListView):
	model = Part
	template_name = 'parts/WG.html'
	context_object_name = 'WG_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='WG').filter(inventory__gt=0)

class MCView(generic.ListView):
	model = Part
	template_name = 'parts/MC.html'
	context_object_name = 'MC_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='MC').filter(inventory__gt=0)

class TMView(generic.ListView):
	model = Part
	template_name = 'parts/TM.html'
	context_object_name = 'TM_parts'

	def get_queryset(self):
		"""
		Excludes any questions not in the category selected.
		"""
		return Part.objects.filter(category='TM').filter(inventory__gt=0)

class DetailView(generic.DetailView):
	model = Part
	template_name = 'parts/detail.html'

	def get_queryset(self):
		"""
		Shows in stock parts again, but unordered
		"""
		return Part.objects.filter(inventory__gt = 0)

class OrderSuccessView(generic.DetailView):
	model = Part
	template_name = 'parts/order_success.html'

class OrderPage(generic.DetailView):
	model = Part
	template_name = 'parts/order_page.html'

def purchase(request, part_id):

	part = get_object_or_404(Part, pk=part_id)

	try:
		selected_part = part
	except (KeyError, Part.DoesNotExist):

		return render(request, 'parts/order_page.html', {
			'part': part,
			'error_message': "This part does not exist or is not in stock.",
			})
	else:
		if selected_part.inventory > 0: 
			selected_part.inventory = selected_part.inventory - 1
			selected_part.save()

			return HttpResponseRedirect(reverse('parts:order_success', args=(part.id,)))
		else:
			return render(request, 'parts/order_page.html', {
			'part': part,
			'error_message': "This part does not exist or is not in stock.",
			})

		return HttpResponseRedirect(reverse('parts:order_success', args=(part.id,)))


# Create your views here.
