import sys, os
import time
print(sys.path)

print("os.path.abspath(\".\") = ", os.path.abspath("."))
print("os.path.base.name(\".\") = ", os.path.basename("."))
print("os.path.getatime(\".\") = ", time.ctime(os.path.getatime(".")))
print("os.path.getmtime(\".\") = ", time.ctime(os.path.getmtime(".")))
print("os.path.getctime(\".\") = ", time.ctime(os.path.getctime(".")))
print("os.path.getsize(\".\") = ", os.path.getsize("."))

print("os.path.isfile(\".\") = ", os.path.isfile("."))
print("os.path.isdir(\".\") = ", os.path.isdir("."))
print("os.path.islink(\".\") = ", os.path.islink("."))
print("os.path.ismount(\".\") = ", os.path.ismount("."))

path = os.path.abspath(".")

print("os.path.joni(path, \"sys_t.py\") = ", os.path.join(path, "sys_t.py"))
print("os.path.normcase(path) = ", os.path.normcase(path))
print("os.path.normpath(path) = ", os.path.normpath(path))
print("os.path.realpath(\".\") = ", os.path.realpath("."))
print("os.path.relpath(path[:5]) = ", os.path.relpath(path[:5]))

fp = open("re_.py","r")
lines = fp.readlines()
for l in lines:
    print(l)
fp.close()


