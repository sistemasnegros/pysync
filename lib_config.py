# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import sys

import logging

ERROR_LOAD_CONFIG = "No se puedo cargar el archivo de configuracion: {}"
INFO_LOAD_CONFIG = "Cargado archivo de configuracion: {}"


def load_config(name_file):
    config = ConfigParser()

    if config.read(name_file) == []:
        logging.error(ERROR_LOAD_CONFIG.format(name_file))

        print ERROR_LOAD_CONFIG.format(name_file)
        sys.exit(0)

    else:
        logging.info(INFO_LOAD_CONFIG.format(name_file))
        return config
