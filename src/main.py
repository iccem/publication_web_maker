# import pipelines
# import images_list_maker
# import FTP_upload
# from doc import doc


if __name__ == '__main__':

    #  Change current number.
    current_year = '2024'
    current_number = '06'

    # ============================================================
    # pipelines.create_pdf_preview(current_year, current_number)
    #
    # pipelines.create_cover_preview_web(current_number)
    #
    # pipelines.open_indd_for_creating_prod_pdf(current_number)
    #
    # print('Then Package created, we have Link dir.')
    # print('Switch back')
    # print('Press any key for continue')

    # ============================================================

    ###  Now indesign opens original file.  I have to make Package and
    ###  then close the file.  Open indd-file from Package directory.
    ###  Change gray photos to color photos.
    ###  The path for directory of temp-photos: D:\!_ПЛАНШЕТ\temp_imgs.

    # pipelines.change_photos(current_year, current_number)
    #
    # print('And then...  Press any key for continue...')

    # ============================================================

    ### Make PDF-file for web and send to the FTP.

    # pipelines.create_prod_pdf(current_number)
    #
    # dir_target = doc._dir_target + '\\' + current_number
    # FTP_upload.pdf_upload(dir_target, current_number)
    # print('Done')

    # ============================================================

    # pipelines.split_pdf_for_pages()
