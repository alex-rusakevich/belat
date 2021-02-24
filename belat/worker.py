import json
import importlib

class Worker:
    LTC = "Lat-to-cyr"
    CTL = "Cyr-to-lat"
    
    @staticmethod
    def get_schemes_from_json(log):
        cfg = ""
        with open("config.json", "r", encoding="utf8") as f:
            cfg = json.load(f)
        schemes = []

        for i in cfg["schemes"]:
            try:
                lib = importlib.import_module("belat."+i)
                schemes.append(lib.Scheme(log))
            except Exception as e:
                if hasattr(e, 'message'):
                    log("Error while loading "+i+": \n"+str(e.message))
                else:
                    log("Error while loading "+i+": \n"+str(e)+"\n")
        return schemes

    def __init__(self, GUI, file_in, file_out, enc_in, enc_out, transform_direction):
        self.GUI = GUI