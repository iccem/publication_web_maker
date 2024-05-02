import os
from PIL import Image


class Cropper:
    def __int__(self, folder: str, target_w: int, target_h: int):
        """
        Crops and resizes JPEG images in a folder, saving the results as PDF and JPEG.
        :param folder:
        :param target_w:
        :param target_h:
        :return:
        """
        self._folder = folder
        self._target_w = target_w
        self._target_h = target_h

    def crop(self, _folder):
        try:
            with os.scandir(_folder) as files_list:
                for file in files_list:
                    if file.is_file() and 'jpg' in file.name and 'ВКЛАДКА' not in file.name:
                        pages = ''.join(filter(str.isdigit, str(file.name)))

                        img = Image.open(_folder + '\\' + file.name)
                        w, h = img.size
                        half = int(w/2)

                        new_img_left = img.crop((0, 0, half, h))
                        new_img_left_new_size = new_img_left.resize((self._target_w, self._target_h))
                        new_img_left_new_size.save(_folder + '\\' + 'cover_' + pages[0] + '.pdf')

                        new_img_right = img.crop((half, 0, w, h))
                        new_img_new_size = new_img_right.resize((self._target_w, self._target_h))
                        new_img_new_size.save(_folder + '\\' + 'cover_' + pages[1] + '.pdf')
                        new_img_new_size.save(_folder + '\\' + 'cover_' + pages[1] + '.jpg')

                    if file.is_file() and 'jpg' in file.name and 'ВКЛАДКА' in file.name:
                        w, h = img.size
                        if w > h:
                            pass

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except PermissionError as e:
            print(f"Error: Permission denied - {e}")
        except Exception as e:
            print(f"An unexpected error occurred - {e}")

        print('Done!')

