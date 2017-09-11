# -*- encoding: utf-8 -*-
import json
from .models import Asset, Server, Manufactory, CPU, Disk, NIC, RAM

class Asset(object):
	
	def __init__(self, request):
		self.request = request
		self.mandatory_fields = ['sn', 'asset_id', 'asset_type']
		self.field_sets = {
			'asset': ['manufactory'],
			'server': ['model', 'cpu_count', 'cpu_core_count', 'cpu_model', 'raid_type', 'os_type', 'os_distribution', 'os_release'],
			'networkdevice': []
		}
		self.response = {
			'error': [],
			'info': [],
			'warning': [],
		}

	def response_msg(self, msg_type, key, msg):
		if self.response.has_key(msg_type):
			self.response[msg_type].append({key: msg})
		else:
			raise ValueError

	def mandatory_check(self, data, only_check_sn=False):
		for filed in self.mandatory_fields:
			if not field in data:
				self.response_msg('error', 'MandatoryCheckFailed', 'The field [%s] is mandatory and not provided in your reporting data' % field)
		else:
			if self.response['error']:
				return False

		try:
			if not only_check_sn:
				self.asset_obj = Asset.objects.get(int(data['asset_id']),sn=data['sn'])			
			else:
				self.asset_obj = Asset.objects.get(sn=data['sn'])
			return True
		except ObjectDoesNotExist as e:
			self.response_msg('error', 'AssetDataInvalid', 'Cannot find asset object')
			self.waiting_approval = True
			return False


	def get_asset_id_by_sn(self):
		pass

	def save_new_asset_to_approval_zone(self):
		pass

	def data_is_valid(self):
		data = self.request.POST.get("asset_data")
		if data:
			try:
				data = json.loads(data)
				self.mandatory_check(data)
				self.clean_data = data
				if not self.response['error']:
					return True
			except ValueError as e:
				self.response_msg('error', 'AssetDataInvalid', str(e))
		else:
			self.response_msg('error', 'AssetDataInvalid', 'The reported asset data is not valid or provided')


	def __is_new_asset(self):
		if not hasattr(self.asset_obj, self.clean_data['asset_type']):
			return True
		else:
			return False


	def data_inject(self):
		if self.__is_new_asset():
			print('\033[32;1m --- new asset, going to create --- \033[0m')
			self.create_asset()
		else:
			print('\033[33;1m --- asset already exist, going to update --- \033[0m')
			self.update_asset()


	def __verify_field(self, data_set, field_key, data_type, required=True):
		field_val = data_set.get(field_key)
		if field_val:
			try:
				data_set[field_key] = data_type[field_val]
			except ValueError as e:
				self.response_msg('error', 'InvalidField', "The field [%s]'s data type ")
		elif required == True:
			self.response_msg('error', 'LackOfField', "The field [%s] has no value")





	def create_asset(self):
		func = getattr(self, '_create_%s' % self.clean_data['asset_type'])
		create_obj = func()


	def update_asset(self):
		func = getattr(self, '_update_%s' % self.clean_data['asset_type'])
		create_obj = func()


	def _update_server(self):
		nic = self.__update_asset_component()


	def _create_server(self):
		self.__create_server_info()
		self.__create_or_update_manufactory()

		self.__create_cpu_component()
		self.__create_disk_component()
		self.__create_nic_component()
		self.__create_ram_component()

		log_msg = "Asset [<a href='/admin/assets/asset/%s' target='_blank'>%s</a>]"
		self.response_msg('info', 'NewAssetOnline', log_msg)


	def __create_server_info(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, 'model', str)
			if not len(self.response['error']) or ignore_errs == True:
				data_set = {
					'asset_id': self.asset_obj.id,
					'raid_type': self.clean_data.get('raid_type'),
					'model': self.clean_data.get('model'),
					'os_type': self.clean_data.get('os_type'),
					'os_distribution': self.clean_data.get('os_distribution'),
					'os_release': self.clean_data.get('os_release'),
				}

				obj = Server(**data_set)
				obj.save()
				return obj
		except Exception as e:
			self.response_msg('error', 'ObjectCreationException', 'Object [server] %s' % )


	def __create_or_update_manufactory(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, 'manufactory', str)
			manufactory = self.clean_data.get('manufactory')
			if not len(self.response['error']) or ignore_errs == True:
				obj_exist = Manufactory.objects.filter(manufactory=manufactory)
				if obj_exist:
					obj = obj_exist[0]
				else:
					obj = Manufactory(manufactory=manufactory)
					obj.save()
				self.asset_obj.manufactory = obj
				self.asset_obj.save()
		except Exception as e:
			self.response_msg('error', 'ObjectCreationException', 'Object [manufactory]')


	def __create_cpu_component(self, ignore_errs=False):
		try:
			self.__verify_field(self.clean_data, 'model', str)
			self.__verify_field(self.clean_data, 'cpu_count', int)
			self.__verify_field(self.clean_data, 'cpu_core_count', int)
			if not len(self.response['error']) or ignore_errs == True:
				data_set = {
					'asset_id': self.asset_obj.id,
					'cpu_model': self.clean_data.get('cpu_model'),
					'cpu_count': self.clean_data.get('cpu_count'),
					'cpu_core_count': self.clean_data.get('cpu_core_count'),
				}

				obj = CPU(**data_set)
				obj.save()
				log_msg = "Asset[%s] ---> has added now [cpu] component with data [%s]" 
				self.response_msg('info', 'NewComponentAdded', log_msg)
				return obj
		except Exception as e:
			self.response_msg('info', 'NewComponentAdded', log_msg)


	def __create_disk_component(self):
		disk_info = self.clean_data.get('physical_disk_driver')
		if disk_info:
			for disk_item in disk_info:
				try:
					self.__verify_field(disk_item, 'slot', str)
					self.__verify_field(disk_item, 'capacity', float)
					self.__verify_field(disk_item, 'iface_type', str)
					self.__verify_field(disk_item, 'model', str)
					if not len(self.response['error']):
						data_set = {
							'asset_id': self.asset_obj.id,
							'sn': disk_item.get('sn'),
							'slot': disk_item.get('slot'),
							'capacity': disk_item.get('capacity'),
							'model': disk_item.get('model'),
							'iface_type': disk_item.get('iface_type'),
							'manufactory': disk_item.get('manufactory'),
						}

						obj = Disk(**data_set)
						obj.save()

				except Exception as e:
					self.response_msg('error', 'ObjectCreationException', 'Object')
		else:
			self.response_msg('error', 'LackOfData', 'Disk info is not provided in your reporting data')



	def __create_nic_component(self):
		nic_info = self.clean_data.get('nic')
		if nic_info:
			for nic_item in nic_info:
				try:
					self.__verify_field(nic_item, 'macaddress', str)
					if not len(self.response['error']):
						data_set = {
							'asset_id': self.asset_obj.id,
							'name': nic_item.get('name'),
							'sn': nic_item.get('sn'),
							'macaddress': nic_item.get('macaddress'),
							'ipaddress': nic_item.get('ipaddress'),
							'bonding': nic_item.get('bonding'),
							'model': nic_item.get('model'),
							'netmask': nic_item.get('netmask'),
						}

						obj = NIC(**data_set)
						obj.save()

				except Exception as e:
					self.response_msg('error', 'ObjectCreationException', 'Object')
		else:
			self.response_msg('error', 'LackOfData', 'NIC info is not provided')


	def __create_ram_component(self):
		ram_info = self.clean_data.get('ram')
		if ram_info:
			for ram_item in ram_info:
				try:
					self.__verify_field(ram_item, 'capacity', int)
					if not len(self.response['error']):
						data_set = {
							'asset_id': self.asset_obj.id,
							'slot': ram_item.get('slot'),
							'sn': ram_item.get('sn'),
							'capacity': ram_item.get('capacity'),
							'model': ram_item.get('model'),
						}

						obj = RAM(**data_set)
						obj.save()

				except Exception as e:
					self.response_msg('error', 'ObjectCreationException', 'Object')
		else:
			self.response_msg('error', 'LackOfData', 'RAM info is not provided')


	def __update_server_component(self):
		pass






























