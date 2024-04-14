import win32com.client
import os

class ConverterINDD2PDF:
    """Open indd-file and create PDF-preview (block)."""
    def __int__(self, folder: str):
        self._folder = folder

    def convert(self):
        this_file = ''
        with os.scandir(self._folder) as files_list:
            for file in files_list:
                if file.is_file() and 'indd' in file.name:
                    print(file.name)
                    this_file = str(file.name)
        app = win32com.client.Dispatch('InDesign.Application.CS3')

        indd_file_path = self._folder + '\\' + this_file
        indd_ = app.Open(indd_file_path)

        pdf_file = self._folder + '\\' + this_file[0:-5] + '.pdf'
        directory = os.path.dirname(pdf_file)

        ID_PDF_TYPE = 1952403524  # Export to PDF

        # 1=[High Quality Print], 2=[PDF/X-1a:2001] etc..
        # 6 is quality - smallest 8 = "2540", 9 = '2540 no marks', 7 - web
        pdf_preset = app.PDFExportPresets.Item(7)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            if os.path.exists(directory):
                indd_.Export(ID_PDF_TYPE, pdf_file, False, pdf_preset)
        except Exception as e:
            print('Export to PDF failed: ' + str(e))
        indd_.Close()
        print('PDF has created.')
