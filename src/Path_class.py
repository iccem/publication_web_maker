from doc import doc


class Path:
    """
    Дано
        публикация indd Чб - путь к файлу
        обложка цветная pdf - путь к папке с файлами pdf
        папка с цветными фото - путь к папке с файлами (jpg, png, etc.)

    Получить
        1) preview-публикация (indd-публикация Чб + "легкая" цветная обложка)
        требуется: чб-публикация, обложка
    """

    #  Source.
    bw_indd_file_path = ''
    cover_hq_files_directory_path = ''
    photos_directory_path = ''

    def _get_paths(self):
        """Get paths sources and targets."""
        dir_source = doc._dir_source_indd + self._current_year + '\\' + self._current_number
        dir_cover_source = doc._dir_cover_source + '\\' + self._current_number

        bw_indd_file_path = self._current_number + doc._tail_of_filename_publication

        dir_target = doc._dir_target + '\\' + self._current_number
        dir_target_cover = doc._dir_target + '\\' + self._current_number + '\\' + 'cover'

        path_cover_1_good_txt = doc._path_cover_1_good_txt

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


path = Path('2024', '08')


