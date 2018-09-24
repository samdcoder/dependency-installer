import os
import subprocess
dependencies_list = []
error_list = []

#get_absolute_name returns absolute name without version numbers
def get_absolute_name(package_list):
	absolute_list = []
	for package in package_list:
		if '=' in package:
			index = package.find('=')
			absolute_list.append(package[0:index])
		else:
			absolute_list.append(package)

	return absolute_list

#reading from file and creating a list of dependencies
with open("dependencies.json", "r") as f:
	for line in f:
		my_str = line.strip()
		if '{' in my_str or '}' in my_str:
			continue
		my_str = my_str.replace(',', '')
		if len(my_str) != 0:
				dependencies_list.append(my_str)

#installing every package according to the dependency list
for package in dependencies_list:
	cmd = 'pip install '+package;
	try: 
		os.system(cmd)
	except:
		print('error')
		
#getting list of all the installed packages
installed = subprocess.run(['pip', 'freeze', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
installed_list = installed.split()

#getting absolute name of each package
absolute_dependency_list = get_absolute_name(dependencies_list)
absolute_installed_list = get_absolute_name(installed_list)


for package in absolute_dependency_list:
	if package not in absolute_installed_list:
		error_list.append(package)

if len(error_list) > 0:
	print("The following packages were not installed: ")
	for e in error_list:
		print(e)
else:
	print("All the packages were successfully installed!") 	

