COMMAN_CHAR_MAX_LENGTH = 512
COMMAN_DEFAULT_NULL_CONFIG = {
    "default":None,
    "null":True
}
COMMAN_DEFAULT_NULL_BLANK_CONFIG = {
    **COMMAN_DEFAULT_NULL_CONFIG,
    "blank":True
}

def storage_file_path(instance, filename):
    return f"{instance.__class__.__name}/{filename}".lower()