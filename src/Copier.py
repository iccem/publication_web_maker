import os
import shutil
from doc import doc


class CurrentPathsMaker:
    def __init__(self, current_number: str):
        self._current_number = current_number

    def get_paths(self):
        current_publication = self._current_number + doc._current_publication
        indd_source = doc.dir_source + '\\' + current_publication
        indd_target = doc.dir_target + '\\' + current_publication

        cover_dir_source = ''
        cover_dir_target = ''

        photos_dir_source = ''


class Copier:
    def __int__(self):
        pass

    def get_copy_file(self, filefrom: str, fileto: str):
        """Copy the file."""
        try:
            shutil.copy(filefrom, fileto)  # копируем публикацию
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
