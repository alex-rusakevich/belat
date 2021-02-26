import importlib

def log(msg):
    print(msg)

lib = importlib.import_module("belat."+input("module: "))
dircn = input("direction: ")
if dircn == "ctl":
    print(lib.Scheme(log).cyr_to_lat(input("text: ")))
elif dircn == "ltc":
    print(lib.Scheme(log).lat_to_cyr(input("text: ")))
