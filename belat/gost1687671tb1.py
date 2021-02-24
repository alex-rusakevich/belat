import belat.scheme as bs

class Scheme(bs.Scheme):
    
    name = "ГОСТ 16876-71 (табл. 1)"
    
    def __init__(self, log):
        self.log = log

    def cyr_to_lat(self, text_in):
        return ""

    def lat_to_cyr(self, text_in):
        return ""
