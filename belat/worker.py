from bs4 import BeautifulSoup
import xml.etree.ElementTree as et
import zipfile
import shutil
import os.path
import os
import re
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

    def __init__(self, file_in, file_out, enc_in, enc_out, transform_direction, scheme, file_type, version):
        self.file_in = file_in
        self.file_out = file_out
        self.enc_in = enc_in
        self.enc_out = enc_out
        self.transform_direction = transform_direction
        self.scheme = scheme
        self.file_type = file_type
        self.version = version

    def work(self):
        if self.file_type == "txt":
            txt = open(self.file_in, "r", encoding=self.enc_in).read()
            
            if self.transform_direction == self.CTL:
                txt = self.scheme.cyr_to_lat(txt)
            elif self.transform_direction == self.LTC:
                txt = self.scheme.lat_to_cyr(txt)
            
            open(self.file_out, "w", encoding=self.enc_out).write(txt)
        elif self.file_type == "epub":
            with zipfile.ZipFile(self.file_in, "r") as zf:
                zf.extractall("__TEMP__")

                root_node = et.parse(os.path.join("__TEMP__", "META-INF", 
                    "container.xml")).getroot()

                full_path = root_node[0][0].attrib["full-path"]

                files_dir = os.path.join("__TEMP__", os.path.split(full_path)[0])

                # Транслітуем імя аўтара, назву кнігі і г.д.
                f = open(os.path.join(files_dir,"content.opf"), "r", encoding=self.enc_in)
                text = f.read()
                soup = BeautifulSoup(text, features="xml")

                if self.transform_direction == self.CTL:
                    soup.find("dc:title").string = self.scheme.cyr_to_lat(soup.find("dc:title").string)
                    for i in soup.find_all("dc:creator"):
                        i.string = self.scheme.cyr_to_lat(i.string)
                elif self.transform_direction == self.LTC:
                    soup.find("dc:title").string = self.scheme.lat_to_cyr(soup.find("dc:title").string)
                    for i in soup.find_all("dc:creator"):
                        i.string = self.scheme.lat_to_cyr(i.string)

                # Дабаўляем тэг
                tag = soup.new_tag("dc:subject")
                tag.string = "be_lat"
                soup.find("metadata").append(tag)

                f.close()
                xhtml = soup.prettify()
                with open(os.path.join(files_dir,"content.opf"), "w", encoding=self.enc_out) as file:
                    file.write("<!--@belat: "+self.version+"-->\n")
                    file.write(xhtml)
                # ==========================================

                xhtml_files = []
                for dir_file in os.listdir(files_dir):
                    if dir_file[dir_file.rindex("."):].lower() == ".xhtml":
                        xhtml_files.append(os.path.join(files_dir, dir_file))

                # Working with a file
                for xhtml_file in xhtml_files:
                    f = open(xhtml_file, "r", encoding=self.enc_in)
                    text = f.read()
                    soup = BeautifulSoup(text, features="xml")

                    if self.transform_direction == self.CTL:
                        for p in soup.find_all("p"):
                            if p.string:
                                p.string.replace_with(self.scheme.cyr_to_lat(p.string))
                            for c in p.contents:
                                c.string.replace_with(self.scheme.cyr_to_lat(c.string))
                    elif self.transform_direction == self.CTL:
                        for p in soup.find_all("p"):
                            if p.string:
                                p.string.replace_with(self.scheme.lat_to_cyr(p.string))
                            for c in p.contents:
                                c.string.replace_with(self.scheme.cyr_to_lat(c.string))
                    f.close()

                    xhtml = soup.prettify()
                    with open(xhtml_file, "w", encoding=self.enc_in) as file:
                        file.write("<!--@belat: "+self.version+"-->\n")
                        file.write(xhtml)

                with zipfile.ZipFile(self.file_out, "w", zipfile.ZIP_DEFLATED) as zf:
                    for root, dirs, files in os.walk("__TEMP__"):
                        for file in files:
                            zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join("__TEMP__")))

                shutil.rmtree("__TEMP__")

