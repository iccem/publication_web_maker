from doc import doc


class Path:
    """
    Дано
        публикация indd Чб - путь к файлу
        обложка цветная pdf - путь к папке с файлами pdf
        папка с цветными фото - путь к папке с файлами (jpg, png, etc.)

    Получить
        preview-публикация (indd-публикация Чб + "легкая" цветная обложка)
    """

    def __int__(self, current_year: str, current_number: str):
        self._current_year = current_year
        self._current_number = current_number

    def get_paths(self):
        """Get paths sources and targets."""
        dir_source = doc._dir_source + self._current_year + '\\' + self._current_number
        dir_cover_source = doc._dir_cover_source + '\\' + self._current_number
        current_publication = self._current_number + doc._current_publication
        dir_target = doc._dir_target + '\\' + self._current_number
        dir_target_cover = doc._dir_target + '\\' + self._current_number + '\\' + 'cover'
        path_cover_1_good_txt = doc._path_cover_1_good_txt
