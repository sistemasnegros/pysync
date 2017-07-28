# -*- coding: utf-8 -*-


import os
import logging


#import pdb

ERROR_RUN_COMMAND = "Al ejecutar comando: {}"
ERROR_VALID_PATH = "Rutas no disponibles: {} o {}"


def copy_mirror(**kwargs):
    """variables:source_path, destiny_path, copy_options"""

    logging.info('Generando comando para el mirror.')

    destiny_path = kwargs.pop("destiny_path")
    source_path = kwargs.pop("source_path")
    copy_options = kwargs.pop("copy_options")

    binary = kwargs.pop("binary")
    format_command = kwargs.pop("format_command")

    if not os.path.exists(source_path) or not os.path.exists(destiny_path):

        logging.error(ERROR_VALID_PATH.format(source_path, destiny_path))
        return

    format_command = format_command.replace("binary", binary)
    format_command = format_command.replace("source_path", source_path)
    format_command = format_command.replace("destiny_path", destiny_path)
    comando = format_command.replace("copy_options", copy_options)

    # if os.name == 'nt':
    #     comando = "robocopy %s %s %s" % (copy_options, source_path, destiny_path)
    # else:
    #     comando = "rsync %s %s %s" % (copy_options, source_path, destiny_path)

    return comando
