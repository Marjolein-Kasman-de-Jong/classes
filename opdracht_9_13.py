# Opdracht 9-13 OrderedDict herschrijven

from collections import OrderedDict

words = OrderedDict()

words['een'] = 'one' 
words['twee'] = 'two' 
words['drie'] = 'three' 
words['vier'] = 'four' 
words['vijf'] = 'five' 
words['zes'] = 'six' 
words['zeven'] = 'seven' 
words['acht'] = 'eight' 
words['negen'] = 'nine' 
words['tien'] = 'ten' 

for key, value in words.items():
    print(key.title() + " is in het Engels " + value + ".")

 