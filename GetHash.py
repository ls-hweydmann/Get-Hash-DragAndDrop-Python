import os, sys, subprocess
import threading 
import pyperclip



def getHash(pathj):
    return subprocess.check_output(f"certutil -hashfile \"{path}\" SHA256 | findstr /v hash", shell=True).decode("utf-8") 

def threadTarget(path, clip):
    clip.append(getHash(path))

clip = []
threads = []

for path in sys.argv[1:]:
    print(path)
    t = threading.Thread(target=threadTarget,args=(path, clip))
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join();

toCopy = ""
for c in clip:
    print(c)
    toCopy += c + "\n";

pyperclip.copy(toCopy)

os.system("pause")

