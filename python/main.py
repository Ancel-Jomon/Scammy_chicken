import subprocess
import sys

def run_with_subprocess():
    
    process1 = subprocess.Popen([sys.executable, 'catch_the_chicken.py'])
    process2 = subprocess.Popen([sys.executable, 'servicefake.py'])
    
    
    process1.wait()
    process2.wait()
run_with_subprocess()