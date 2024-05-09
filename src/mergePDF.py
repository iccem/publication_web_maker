import os
import shutil
from PyPDF2 import PdfWriter


class PDFmerger:
    def merge(self, dir_target: str, dir_target_cover: str, current_number: str, path_cover_1_good_txt: str):
        """
        Merge multiple PDF files into a single preview PDF file.
        :param dir_target:
        :param dir_target_cover:
        :param current_number:
        :param path_cover_1_good_txt:
        :return:
        """
        # Copy the first cover PDF
        first_cover_pdf_source = os.path.join(path_cover_1_good_txt, current_number, 'обложка', 'SamOboz_1.pdf')
        first_cover_pdf = os.path.join(dir_target_cover, 'cover_1.pdf')
        try:
            shutil.copy(first_cover_pdf_source, first_cover_pdf)
            print('Cover has copied!')
        except Exception as e:
            print(f'Export to PDF failed: {e}')

        # Collect the PDF files to be merged
        block_pdf = os.path.join(dir_target, [f for f in os.listdir(dir_target) if f.endswith('.pdf')][0])
        cover_pdf_list = [os.path.join(dir_target_cover, f) for f in os.listdir(dir_target_cover) if
                          f.endswith('.pdf') and 'cover' in f]

        # Merge the PDFs
        merger = PdfWriter()
        with open(cover_pdf_list[0], "rb") as input1, \
                open(cover_pdf_list[1], "rb") as input2, \
                open(block_pdf, "rb") as input_block, \
                open(cover_pdf_list[2], "rb") as input3, \
                open(cover_pdf_list[3], "rb") as input4:
            merger.append(input1)
            merger.append(input2)
            merger.append(input_block)
            merger.append(input3)
            merger.append(input4)
            merger.write(os.path.join(dir_target, f"{current_number}-preview.pdf"))
        merger.close()