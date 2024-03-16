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

    def get_copy_file(self):
        """Copy the file."""
        try:
            shutil.copy(self._filefrom, self._fileto)  # копируем публикацию
            print('Indd has copied!')
        except:
            print('err')

    def get_file_folder(self):
        """Copy the cover files folder."""
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
