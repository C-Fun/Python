import os

path=input("����һ��·��")
for root, dirs, files in os.walk(path):
    for name in files:
        fname, fext = os.path.splitext(name)
        os.rename(os.path.join(root, name),\
                  os.path.join(root, fname+'_py'+fext))
