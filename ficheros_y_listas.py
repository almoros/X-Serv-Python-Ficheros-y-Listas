#!/usr/bin/python3

myfile = open('/etc/passwd','r')
machines = myfile.readlines()
counter = 1;

for users in machines:
    divide_machines = users.split(':')
    print ("La máquina " + str(counter) + " es: " + divide_machines[0] + " y la shell que utiliza es: " + divide_machines[-1])
    counter += 1

print ("En total tenemos " + str(counter - 1) + " máquinas")

myfile.close()
