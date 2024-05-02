import os
from pdf2image import convert_from_path


class Pdf2jpeg:
    def __init__(self, poppler_path: str):
        """
        Initializes the Pdf2jpeg class with the path to the Poppler installation.
        """
        self._poppler_path = poppler_path

    def convert(self, dir_target: str):
        """
        Converts every pdf in directory to jpeg.
        """
        with os.scandir(dir_target) as files_list:
            for file in files_list:
                if file.is_file() and 'pdf' in file.name:
                    print(file.name)
                    pdffile = os.path.join(dir_target, file.name)
                    images = convert_from_path(pdffile, 96, self._poppler_path)

                    for i in range(len(images)):
                        images[i].save(os.path.join(dir_target, f"{file.name}.jpg"), 'JPEG')
