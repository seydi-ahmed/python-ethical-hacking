import subprocess
# subprocess.call("COMMAND", shell=True1)
subprocess.call("ls -a", shell=True)

age = input("what is your age?")
if age == 12:
    subprocess.call("ls", shell=True)
elif age == 13:
    subprocess.call("ls -R", shell=True)
else:
    subprocess.call("ls -r", shell=True)