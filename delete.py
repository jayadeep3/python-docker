import subprocess
image = input("Enter the image name to be deleted: ")
subprocess.call("docker rmi -f %s"%image,shell=True)
