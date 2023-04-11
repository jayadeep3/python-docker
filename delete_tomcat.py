import subprocess
subprocess.call('docker container ls | grep catalina.sh | cut -d " " -f 1 >file1',shell=True)

file1 = open("file1","r")
image_ids = file1.readlines()
i = 0
while i < len(image_ids):
    image = image_ids[i]
    subprocess.call("docker rm -f %s"%image,shell=True)
    i = i + 2
