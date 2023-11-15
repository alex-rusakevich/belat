import importlib

from belat import settings


def log(msg):
    print(msg)


lib = importlib.import_module("belat." + input(f"Module name: ").lower().strip())
dircn = input("Direction (cyr-to-lat (ctl) or lat-to-cyr (ltc)): ").lower().strip()

if dircn in ("ctl", "cyr-to-lat"):
    print(lib.Scheme(log).cyr_to_lat(input("Result: ")))
elif dircn in ("ltc", "lat-to-cyr"):
    print(lib.Scheme(log).lat_to_cyr(input("Result: ")))
