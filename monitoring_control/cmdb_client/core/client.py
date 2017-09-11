# -*- encoding: utf-8 -*-
from conf import settings
import urllib, sys, os, json, datetime
from core import info_collection
# import api_token

class ClientHandler(object):

	def __init__(self, argv_list):
		self.argvs = argv_list
		self.parse_argv()

	def collect_data(self):
		obj = info_collection.InfoCollection()
		asset_data = obj.collect()
		print(asset_data)

	def run_forever(self):
		pass

	def __attach_token(self, url_str):
		pass

	def __submit_data(self, action_type, data, method):
		if action_type in settings.Params['urls']:
			if type(settings.Params['port']) is int:
				url = "http://%s:%s%s" % (settings.Params['server'],settings.Params['port'],settings.Params['urls'])
			else:
				url = "http://%s%s" % (settings.Params['server'],settings.Params['urls'][action_type])

			url = self.__attach_token(url)
			print('Connecting [%s], it may take a minute' % url)

			if method == "get":
				args = ""
				for k, v in data.items():
					args += "&%s=%s" % (k, v)
				args = args[1:]
				url_with_args = "%s?%s" % (url, args)
				try:
					req = urllib.Request(url_with_args)
					req_data = urllib.urlopen(req, timeout=settings.Params['request_timeout'])
					callback = req_data.read()
					print("----> server response: ", callback)
					return callback
				except urllib.URLError as e:
					sys.exit("\033[31;1m%s\033[0m" % e)
			elif method == "post":
				try:
					data_encode = urllib.urlencode(data)
					req = urllib.Request(url=url, data=data_encode)
					res_data = urllib.urlopen(req, timeout=settings.Params['request_timeout'])
					callback = res_data.read()
					callback = json.loads(callback)
					print("\033[31;1m[%s]:[%s]\033[0m response:\n%s" % (method, url, callback))
					return callback
				except Exception as e:
					sys.exit("\033[31;1m%s\033[0m" % e)
		else:
			raise KeyError


	def report_asset(self):
		obj = info_collection.InfoCollection()
		asset_data = obj.collect()
		asset_id = self.load_asset_id(asset_data['sn'])
		if asset_id:
			asset_data['asset_id'] = asset_id
			post_url = "asset_report"
		else:
			asset_data['asset_id'] = None
			post_url = "asset_report_with_no_id"

		data = {'asset_data': json.dumps(asset_data)}
		response = self.__submit_data(post_url, data, method="post")
		if "asset_id" in response:
			self.__update_asset_id(response['asset_id'])
		self.log_record(response)


	def log_record(self, log, action_type=None):
		f = open(settings.Params["log_file"], "ab")



	def load_asset_id(self, sn=None):
		asset_id_file = settings.Params['asset_id']
		has_asset_id = False
		if os.path.isfile(asset_id_file):
			asset_id = open(asset_id_file).read().strip()
			if asset_id.isdigit():
				return asset_id
			else:
				has_asset_id = False
		else:
			has_asset_id = False


	def __update_asset_id(self, new_asset_id):
		asset_id_file = settings.Params['asset_id']
		f = open(asset_id_file, 'wb')
		f.write(str(new_asset_id))
		f.close()


	def parse_argv(self):
		pass





















