import os
import shutil


class Copier:
    def __int__(self) -> None:
        # indd file
        # self._filefrom = filefrom
        # self._fileto = fileto
        #
        # # img dir
        # self._imgdirfrom = imgdirfrom
        # self._imgdirto = imgdirto

    # Files.
    def copy_indd_file(self):
        """
        Copy the file.
        """
        try:
            shutil.copy(self._filefrom, self._fileto)  # копируем публикацию
            print('Indd has copied!')
        except:
            print('err')

    def copy_cover_title(self):
        pass

    # Directory.
    def copy_color_dir(self, source_dir: str, target_dir: str) -> None:
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

    def copy_imgs(self):
        pass