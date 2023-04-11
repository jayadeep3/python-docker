import subprocess
image = input("Enter the image name: ")
container = input("Enter the container name: ")
detach = input("Do you want to run in detach mode y/n: ")

if detach == 'y':
    subprocess.call("docker run --name %s -d %s"%(container,image),shell=True)
elif detach == 'n':
    subprocess.call("docker run --name %s  %s"%(container,image),shell=True)
else:
    print("Invalid option")

