class Dataset():
	def __init__(self, name, array):
		self.name = name
		self.array = array

	def H5VL_python_dataset_read(self, connector_id, mem_type_id, mem_space_id, file_space_id, plist_id, req):
		print('Reading dataset ' + self.name + ' = ' + str(self.array))
		return self.array		

	def H5VL_python_dataset_write(self, connector_id, mem_type_id, mem_space_id, file_space_id, plist_id, buf, req):
		print('Writing dataset ' + self.name + ' = ' + str(buf))
		self.array = buf

class Group():
	def __init__(self, name):
		self.name = name
		self.groups = {}
		self.datasets = {}
		
	def H5VL_python_dataset_create(self, loc_params, connector_id, name, dcpl_id, dapl_id, dxpl_id, req):
		print('Creating dataset ' + name)
		dataset = Dataset(name, None)
		self.datasets[name] = dataset
		return dataset

class File():
	def __init__(self, name):
		self.name = name
		self.groups = {'/': Group('/')}

	def H5VL_python_group_open(self, loc_params, connector_id, name, gapl_id, dxpl_id, req):
		print('Opening group ' + name)
		return self.groups[name]

class VOL():
	def __init__(self):
		self.files = {}

	def H5VL_python_file_create(self, name, flags, fcpl_id, fapl_id, dxpl_id, req):
		print('Creating file ' + name)
		new_file = File(name)
		self.files[name] = new_file
		return new_file