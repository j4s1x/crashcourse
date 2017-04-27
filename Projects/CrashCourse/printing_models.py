from printmodels import print_models
from printmodels import show_completed_models as x
#There is a file called printmodels.py which is the module for the functions
#start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#simulate printing each design till there are none left
#move to completed models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate creating 3d printing
    print("Printing model: " + current_design)
    completed_models.append(current_design)
#display all completed models
print('The following models have been printed:')
for completed_model in completed_models:
    print('\t' + completed_model)
#now do this but with a function

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
x(completed_models)
