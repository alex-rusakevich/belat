import json
import importlib
import traceback

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
                log("Error while loading "+i+": \n"+str(traceback.format_exc()))
        return schemes

    def __init__(self, file_in, file_out, enc_in, enc_out, transform_direction, scheme, file_type):
        self.file_in = file_in
        self.file_out = file_out
        self.enc_in = enc_in
        self.enc_out = enc_out
        self.transform_direction = transform_direction
        self.scheme = scheme
        self.file_type = file_type

    def work(self):
        if self.file_type == "txt":
            txt = open(self.file_in, "r", encoding=self.enc_in).read()
            
            if self.transform_direction == self.CTL:
                txt = self.scheme.cyr_to_lat(txt)
            elif self.transform_direction == self.LTC:
                txt = self.scheme.lat_to_cyr(txt)
            
            open(self.file_out, "w", encoding=self.enc_out).write(txt)
