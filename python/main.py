from subprocess import call


import sys

def run_with_subprocess():
    
    call(["python", 'catch_the_chicken.py'])
    call(["python", 'servicefake.py'])
    
    
    
run_with_subprocess()