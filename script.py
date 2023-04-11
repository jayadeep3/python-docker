import subprocess
image = input("Enter the image name to be downloaded: ")
subprocess.call("docker pull %s"%image,shell=True)
