import subprocess

i = 1
while i <=10:
    subprocess.call("docker network create --driver bridge jayadeep%d"%i,shell=True)
    subprocess.call("docker run --name container%d -d -P --network jayadeep%d tomcat"%(i,i),shell=True)
    i = i + 1
