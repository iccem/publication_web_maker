import win32com.client
import os


class ConverterINDD2PDF:
    """
    Convert InDesign files (.indd) to PDF files within a specified folder.
    """
    def __int__(self, folder: str):
        self._folder = folder

    def convert(self):
        indd_folder = self._folder
        indd_file_name = ''
        with os.scandir(indd_folder) as files_list:
            for file in files_list:
                if file.is_file() and 'indd' in file.name:
                    print(file.name)
                    indd_file_name = str(file.name)

        # Initialize InDesign application
        app = win32com.client.Dispatch('InDesign.Application.CS3')

        # Open the InDesign file
        indd_file_path = os.path.join(indd_folder, indd_file_name)
        indd_ = app.Open(indd_file_path)

        # Create the output PDF file path
        pdf_file_name = indd_file_name[0:-5] + '.pdf'
        pdf_file_path = os.path.join(indd_folder, pdf_file_name)

        # Export the InDesign file to PDF
        pdf_preset = app.PDFExportPresets.Item(7)  # Web PDF preset
        try:
            # Create the output directory if it doesn't exist
            output_directory = os.path.dirname(pdf_file_path)
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Export the InDesign file to PDF
            indd_.Export(1952403524, pdf_file_path, False, pdf_preset)  # Export to PDF
        except Exception as e:
            print(f'Export to PDF failed: {str(e)}')

        # Close the InDesign application
        indd_.Close()
        print('PDF has been created.')
