import os
from charms.reactive import when, when_not, set_state
import subprocess

@when_not('layer-jdk-example.installed')
def install_layer_jdk_example():    
    os.getenv("JAVA_HOME")
    # locate / download java file and compile
    sp = subprocess.Popen(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print sp.communicate()
    print sp.wait()
    print subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
    set_state('layer-jdk-example.installed')
