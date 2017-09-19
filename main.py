"""
Generates report from alerts generated by rules
"""

# python modules
import sys

# local modules
import pe

# directory of rules
import rules

# parse the file specified at the comand line
obj = pe.PE(sys.argv[1])

# list holding alerts accross all rules
alerts = []

# loop through each rule in the rules directory
for rule in rules.__all__:
  # import the rule and call the run() function with the parser object
  print('[-] running rule: ' + rule + '...')
  __import__('rules.' + rule)
  alerts.extend(sys.modules['rules.' + rule].run(obj))

# display any alerts sorted by level
print('[-] results:')
print('-' * 80)
for a in alerts:
  print(a)
  # display delimiter
  print('-' * 80)
