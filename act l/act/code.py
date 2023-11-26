from armConvenientTry import *
import subprocess

subprocess.Popen(["C:\\Users\\HP\\Desktop\\act l\\startpage.exe"])
print('_______________________________')
print('   ======   ======  =======')
print('        =   =          =')
print('   ======   =          =')
print('   =    =   =          =')
print('   ======== ======     = ')
print('_______________________________')
n = 0
list_f = []

while True:
    n+=1
    i = input()
    list_f.append(i)
    p = Information()
    p.IntegratedCompilation(i)
    with open('range1mosue2134532aca22p3901t492.Alternatecach'+'.act', "w") as file:
        file.write(str(list_f))




