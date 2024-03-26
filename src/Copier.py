import os
import shutil
from doc import doc


class Path:
    def get_number(self, number: str) -> str:
        """
        проверяет, если 1-9 включительно
        добавляет в начале 0"""
        if len(number) == 1:
            return '0' + number
        return number

    def __init__(self, number: str, year: str):
        self._raw_number = number
        self._year = year

        self._number = self.get_number(self._raw_number)

    def get_path(self):
        # source

        # indd file
        publication_filename = self._number + doc.tail_of_filename_publication
        indd_source = doc.dir_source_indd + + self._year + '\\' + self._number + '\\' + publication_filename

        indd_target = ''

        cover_dir_source = ''
        cover_dir_target = ''

        photos_dir_source = ''

        # target


class Copier:
    def __int__(self, filefrom: str, fileto: str, imgdirfrom: str, imgdirto: str) -> None:
        # indd file
        self._filefrom = filefrom
        self._fileto = fileto

        # img dir
        self._imgdirfrom = imgdirfrom
        self._imgdirto = imgdirto

    def get_copy_indd_file(self):
        """Copy the file."""
        try:
            shutil.copy(self._filefrom, self._fileto)  # копируем публикацию
            print('Indd has copied!')
        except:
            print('err')

    def get_file_cover_folder(self):
        """Copy the cover and extra adv files folder."""
        if not os.path.exists(self._imgdirto):
            os.makedirs(self._imgdirto)
        with os.scandir(self._imgdirfrom) as files_list:
            for file in files_list:
                if file.is_file():
                    print(file.name)
                    try:
                        shutil.copy(self._imgdirfrom + '\\' + file.name, self._imgdirto + '\\' + file.name)
                        # копируем обложку
                        #  обложка большая! копируется медленно!
                        print('Cover has copied!')
                    except Exception as e:
                        print('Export to PDF failed: ' + str(e))

    def copy_cover_files(self, source_dir: str, target_dir: str) -> None:
        """
        Copy cover files from the source directory to the target directory.

        Args:
            source_dir (str): The path to the source directory containing cover files.
            target_dir (str): The path to the target directory where cover files will be copied.

        Returns:
            None
        """
        # Create the target directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)

        # Iterate over files in the source directory
        for file_name in os.listdir(source_dir):
            source_file_path = os.path.join(source_dir, file_name)
            target_file_path = os.path.join(target_dir, file_name)

            # Check if the current item is a file
            if os.path.isfile(source_file_path):
                try:
                    # Copy the file to the target directory
                    shutil.copy(source_file_path, target_file_path)
                    print(f"Cover file '{file_name}' has been copied successfully.")
                except Exception as e:
                    print(f"Error copying cover file '{file_name}': {str(e)}")
