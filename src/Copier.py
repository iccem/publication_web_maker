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
    def __int__(self, filefrom: str, fileto: str) -> None:
        self.filefrom = filefrom
        self.fileto = fileto

    def get_copy_file(self):
        """Copy the file."""
        try:
            shutil.copy(self.filefrom, self.fileto)  # копируем публикацию
            print('Indd has copied!')
        except:
            print('err')

    def get_file_folder(self, dirsource: str, dirto: str):
        """Copy the cover files folder."""
        if not os.path.exists(dirto):
            os.makedirs(dirto)
        with os.scandir(dirsource) as files_list:
            for file in files_list:
                if file.is_file():
                    print(file.name)
                    try:
                        shutil.copy(dirsource + '\\' + file.name, dirto + '\\' + file.name)
                        # копируем обложку
                        #  обложка большая! копируется медленно!
                        print('Cover has copied!')
                    except Exception as e:
                        print('Export to PDF failed: ' + str(e))
