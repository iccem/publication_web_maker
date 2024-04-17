from doc import doc
import os
from pdf2image import convert_from_path


class Pdf2jpeg:

    def convert(dir_target: str):
        """
        Converts every pdf in directory to jpeg.
        Poppler installation path not detected automatically in windows.
        """

        POPPLER_PATH = doc._POPPLER_PATH

        with os.scandir(dir_target) as files_list:
            for file in files_list:
                if file.is_file() and 'pdf' in file.name:
                    print(file.name)
                    pdffile = dir_target + '\\' + file.name
                    images = convert_from_path(pdffile, 96, POPPLER_PATH)

                    for i in range(len(images)):
                        images[i].save(pdffile +'.jpg', 'JPEG')
