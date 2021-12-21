# python-package-template
Template for authomize package.

## Configure New Template
Make sure you configurate the following files:

### Main Folder
- Replace `fill_the_right_name` with the package main folder name (`authomize/{package_main_folder}`)

### setup.py
- Replace `name` with the package name.
- Fill the right description at `description`
- Replace `fill_the_right_name` at `package_data` with the package main folder name (`authomize/{package_main_folder}`)
- Add the right dependecies at `install_requires`

### setup.cfg
- Incase of using `authomize` packages, uncomment `known_third_party` and fill with the right authomize packages

### MANIFEST.in
- Replace `fill_the_right_name` with the package main folder name (`authomize/{package_main_folder}`)

### Jenkinsfile
- Uncomment `build_push_python_package()` if needed
