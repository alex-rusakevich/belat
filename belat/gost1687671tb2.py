import belat.scheme as bs

class Scheme(bs.Scheme):
    name = "ГОСТ 16876-71 (табл. 2)"
    
    def __init__(self, log):
        self.log = log