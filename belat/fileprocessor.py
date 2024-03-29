import os
import os.path
import shutil
import xml.etree.ElementTree as et
import zipfile

from bs4 import BeautifulSoup

import belat
import belat.schemes as bs


class FileProcessor:
    LTC = "Lat-to-cyr"
    CTL = "Cyr-to-lat"

    ALLOWED_EXT = (".txt", ".epub", ".fb2")

    def __init__(
        self,
        file_in: str,
        file_out: str,
        enc_in: str,
        enc_out: str,
        transform_direction: str,
        scheme: bs.Scheme,
        file_type: str,
    ):
        """Initialize the file processor before starting to work

        :param file_in: file path in
        :type file_in: str
        :param file_out: file path out
        :type file_out: str
        :param enc_in: input file's encoding
        :type enc_in: str
        :param enc_out: output file's encoding
        :type enc_out: str
        :param transform_direction: `"Lat-to-cyr"` or `"Cyr-to-lat"`
        :type transform_direction: str
        :param scheme: translation scheme
        :type scheme: bs.Scheme
        :param file_type: one of the types specified in :obj:`belat.fileprocessor.FileProcessor.ALLOWED_EXT`
        :type file_type: str
        """
        self.file_in = file_in
        self.file_out = file_out
        self.enc_in = enc_in
        self.enc_out = enc_out
        self.transform_direction = transform_direction
        self.scheme = scheme
        self.file_type = file_type

    def work(self):
        """Start processing the files previously set in :func:`belat.fileprocessor.FileProcessor.__init__`"""
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

                root_node = et.parse(
                    os.path.join("__TEMP__", "META-INF", "container.xml")
                ).getroot()

                full_path = root_node[0][0].attrib["full-path"]

                files_dir = os.path.join("__TEMP__", os.path.split(full_path)[0])

                # Translit author's and book's name etc
                f = open(
                    os.path.join(files_dir, "content.opf"), "r", encoding=self.enc_in
                )
                text = f.read()
                soup = BeautifulSoup(text, features="xml")

                if self.transform_direction == self.CTL:
                    soup.find("dc:title").string = self.scheme.cyr_to_lat(
                        soup.find("dc:title").string
                    )
                    for i in soup.find_all("dc:creator"):
                        i.string = self.scheme.cyr_to_lat(i.string)
                elif self.transform_direction == self.LTC:
                    soup.find("dc:title").string = self.scheme.lat_to_cyr(
                        soup.find("dc:title").string
                    )
                    for i in soup.find_all("dc:creator"):
                        i.string = self.scheme.lat_to_cyr(i.string)

                # region Adding belat metatags to the file
                tag = soup.new_tag("dc:subject")
                tag.string = "be_lat"
                soup.find("metadata").append(tag)

                f.close()
                xhtml = soup.prettify()
                with open(
                    os.path.join(files_dir, "content.opf"), "w", encoding=self.enc_out
                ) as file:
                    file.write("<!--@belat: " + belat.__version__ + "-->\n")
                    file.write(xhtml)
                # endregion

                xhtml_files = []
                for dir_file in os.listdir(files_dir):
                    if "." in dir_file:
                        if dir_file[dir_file.rindex(".") :].lower() == ".xhtml":
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
                        file.write("<!--@belat: " + belat.__version__ + "-->\n")
                        file.write(xhtml)

                # Packing the files back
                with zipfile.ZipFile(self.file_out, "w", zipfile.ZIP_DEFLATED) as zf:
                    for root, dirs, files in os.walk("__TEMP__"):
                        for file in files:
                            zf.write(
                                os.path.join(root, file),
                                os.path.relpath(
                                    os.path.join(root, file), os.path.join("__TEMP__")
                                ),
                            )

                shutil.rmtree("__TEMP__")

        elif self.file_type == "fb2":
            f_in = open(self.file_in, "r", encoding=self.enc_in).read()
            soup = BeautifulSoup(f_in, features="xml")

            # region Processing meta tags
            for i in soup.find("title-info"):
                if i.name in ["author", "translator", "annotation", "publish-info"]:
                    for k in i:
                        if self.transform_direction == self.CTL:
                            k.string = self.scheme.cyr_to_lat(k.string)
                        elif self.transform_direction == self.LTC:
                            k.string = self.scheme.lat_to_cyr(k.string)
                elif i.name == "book-title":
                    if self.transform_direction == self.CTL:
                        i.string = self.scheme.cyr_to_lat(i.string)
                    elif self.transform_direction == self.LTC:
                        i.string = self.scheme.lat_to_cyr(i.string)
            # endregion

            if self.transform_direction == self.LTC:
                for b in soup.find_all("body"):
                    for p in b.find_all("p"):
                        if p.string:
                            p.string.replace_with(self.scheme.lat_to_cyr(p.string))
                        for c in p.contents:
                            c.string.replace_with(self.scheme.lat_to_cyr(c.string))
                    for p in b.find_all("v"):
                        if p.string:
                            p.string.replace_with(self.scheme.lat_to_cyr(p.string))
                        for c in p.contents:
                            c.string.replace_with(self.scheme.lat_to_cyr(c.string))
            elif self.transform_direction == self.CTL:
                for b in soup.find_all("body"):
                    for p in b.find_all("p"):
                        if p.string:
                            p.string.replace_with(self.scheme.cyr_to_lat(p.string))
                        for c in p.contents:
                            c.string.replace_with(self.scheme.cyr_to_lat(c.string))
                    for p in b.find_all("v"):
                        if p.string:
                            p.string.replace_with(self.scheme.cyr_to_lat(p.string))
                        for c in p.contents:
                            c.string.replace_with(self.scheme.cyr_to_lat(c.string))

            xhtml = soup.prettify()
            with open(self.file_out, "w", encoding=self.enc_out) as file:
                file.write("<!--@belat: " + belat.__version__ + "-->\n")
                file.write(xhtml)
