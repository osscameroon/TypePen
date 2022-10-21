from os.path import expanduser, join

CF_NAME = r"config.ini"

MAIN_WIN_SIZE = (642, 300)

MIN_WIN_SIZE = (700,690)

NEW_WIN_SIZE = (900, 700)

SETTINGS_WIN_SIZE = (450, 300)

CF_SETTING_NAMES = ["TypePenSettings"]

DSL_FOLDER_NAME = "TypePen Notes"

DEFAULT_STORAGE_LOCATION = join(expanduser('~'), "Documents", DSL_FOLDER_NAME)

CF_DEFAULT = {
    "autosave": "false",
    "save_location": DEFAULT_STORAGE_LOCATION,
}