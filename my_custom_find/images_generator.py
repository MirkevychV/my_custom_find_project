from my_custom_find.file_in_path_generator import file_in_path_generator

# Most popular image formats
img_formats = ('.png', '.gif', '.jpg', '.jpeg', '.bmp', '.tif', '.PSD')


def images_generator(path):
    """
    Generates images in path:'path'
    """
    for file in file_in_path_generator(path):
        if file.endswith(img_formats):
            yield file
