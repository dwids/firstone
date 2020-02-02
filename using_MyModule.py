# Import my "hello" module. 2nd test, using a path in the import
# https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
# Note autocompletion finds the module. Nice!
import sys
sys.path.append('C:/Users/DAVID/Dropbox (Personal)/fromWin/src/python/v3/myModules')

import hello

# Call function.  Note autocompletion finds the function. Nice! 
hello.world()

# Print variable that is in the "hello" module. Note autocompletion finds the variable. Nice!    
print(hello.shark)

# Call class. Again autocompletion on the name and the 2 values. Nice!
jesse = hello.Octopus("Jesse","orange")
jesse.tell_me_about_the_octopus()

fred = hello.Octopus("Fred","purple")
fred.tell_me_about_the_octopus()