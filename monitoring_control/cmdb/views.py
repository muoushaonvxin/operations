from django.shortcuts import render, HttpResponse
from django.generic import View
from .ServerHandler import core
import json

# Create your views here.
class AssetReport(View):
	def get(self, request):
		print(request.GET)
		

	def post(self, request):
		ass_handler = core.Asset(request)
		if ass_handler.data_is_valid():
			print('------ asset data valid: ')
			ass_handler.data_inject()
		return HttpResponse(json.dumps(ass_handler.response), content_type="application/json")
























