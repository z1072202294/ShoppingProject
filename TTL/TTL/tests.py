import os,sys



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
print(os.path)
print(sys.path)
sys.path.insert(0,os.path.join(BASE_DIR,'baseApps'))