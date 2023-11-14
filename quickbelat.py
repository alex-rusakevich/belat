import importlib


def log(msg):
    print(msg)


lib = importlib.import_module("belat." + input("module: "))
dircn = input("direction (cyr-to-lat (ctl) or lat-to-cyr (ltc)): ").lower().strip()

if dircn in ("ctl", "cyr-to-lat"):
    print(lib.Scheme(log).cyr_to_lat(input("text: ")))
elif dircn in ("ltc", "lat-to-cyr"):
    print(lib.Scheme(log).lat_to_cyr(input("text: ")))
