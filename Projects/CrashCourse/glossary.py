#call this a glossary.  Five words i've learned in the previous chapters.
#use the words as keys and definitions as values.  use the \n char

glossary = {
'Dictionary:': 'An associative array, where arbitrary keys are mapped to values.',
'Function:': 'A series of statements which returns some value to a caller.  It can be passed zero or more arguments',
'List:': 'A built-in Python sequence.',
'Module:': 'An object that serves as an organizational unit of Python code.  They are loaded by importing.',
'Slice:': 'An object usually containing a portion of a sequence.',
}

for key, value in glossary.items():
    print(key + '\n' + value + '\n')
