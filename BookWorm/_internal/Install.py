import subprocess
import sys
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder_path)

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
except subprocess.CalledProcessError:
    print("Couldn't fetch needed requirements!")
    exit()

print("Requirements Installed")
subprocess.run(["python", "Menu.py"])
