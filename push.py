import subprocess
subprocess.call("git add .", shell=True)
subprocess.call("git commit -m 'auto_push'", shell=True)
subprocess.call("git push", shell=True)