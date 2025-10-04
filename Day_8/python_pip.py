" PIP "

# ? PIP is a package manager for Python

# * What is a package?
# ? A package contains all the files you need for a module
# ? Module are python code libraries which can be included  in you project

# Check if PIP is installed
# ? use  ' pip --version ' in the terminal

# * Download a Package
# ? Go to your script directory
# ? Add the install package command to install the package
# * Syntax: pip install <package_name>

# Example: pip install camelcase

# import the package into your code to use it
""" 
import camelcase

c = camelcase.CamelCase()

txt = "Hello world"

print(c.hump(txt))
 """

# * UNINSTALL PACKAGE
# ? Type "pip uninstall <package_name>" in the terminal

# * LIST PACKAGES
# ? Use the ' list ' command in your terminal
# Syntax: pip list