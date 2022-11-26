from django.views.generic import View
from django.shortcuts import render

# Despues creamos una clases

class HomeView(View):
	def get(self, request, *args, **kwargs):
	
		context = {

	    }
		return render(request, 'index.html',context)
	
	# demos import render()
	# Siempre que retomamos debemos llamar request
	# context = {} Esto es un diccionario
	# return render(request, '', context)
	# from django.shortcuts import render

	# Depues nos vamos a settings.py
	# TEMPLATES = []
	# os.path.join(BASE_DIR, 'template')

    
    