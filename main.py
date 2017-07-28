
# -*- coding: utf-8 -*-

"""
Autor Kevin Franco
modulo principal de windowssyn

"""
# libreria nativas
import logging
import argparse

# mis librerias
from lib_mount import mount_und
from lib_mail import send_mail
from lib_robocopy import copy_mirror
from lib_config import load_config
from lib_command import run_command

#import os


# Librerias de depuracion
#import pdb
# pdb.set_trace()


def loading_args():
    """Argumento de ejecucion"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Mostrar información en consola.", action="store_true")
    parser.add_argument("-c", "--config", help="Nombre de archivo de configuracion.", default="pysync.cfg")
    parser.add_argument("-d", "--debug", help="Mostrar información de depuración.", action="store_true")
    parser.add_argument("-t", "--test", help="Tirar una prueba del comando.", action="store_true")

    args = parser.parse_args()

    return args


def log_configuration(args):
    """Configurando los log"""

    level_log = logging.INFO

    if args.debug:
        level_log = logging.DEBUG

    logformat = "%(asctime)s %(levelname)s: %(message)s"

    logging.basicConfig(filename="pysync.log", filemode='w', format=logformat, level=level_log)

    if args.verbose:
        fh = logging.StreamHandler()
        logFormatter = logging.Formatter(logformat)
        fh.setFormatter(logFormatter)
        logging.getLogger().addHandler(fh)


def fun_mount_und(config):
    if config.get("MOUNT", "enable") == "yes":
        logging.info('Habilitada opcion de montaje de red.')

        comando = mount_und(
            destiny_path=config.get("GENERAL", "destiny_path"),
            username_und=config.get("MOUNT", "username_und"),
            password_und=config.get("MOUNT", "password_und"),
            path_network=config.get("MOUNT", "path_network"),
            letter_und=config.get("MOUNT", "letter_und"),
        )

        if comando:
            run_command(comando)


def fun_send_mail(config, args):
    if config.get("MAIL", "enable") == "yes":

        send_from = config.get("MAIL", "send_from")
        username = config.get("MAIL", "username")
        password = config.get("MAIL", "password")
        send_to = config.get("MAIL", "send_to")

        files = config.get("MAIL", "files")
        if files == "no":
            files = None

        server = config.get("MAIL", "server")
        port = config.get("MAIL", "port")
        tls = config.get("MAIL", "tls")

        with open('pysync.log') as my_file:
            data_log = my_file.read()

        if data_log.find("ERROR") != -1 and not args.debug:
            subject = config.get("MAIL", "subject_error")
        else:
            subject = config.get("MAIL", "subject_ok")

        for email in send_to.split(","):

            try:
                send_mail(
                    username,
                    password,
                    send_from,
                    email.strip(),
                    subject,
                    data_log,
                    files,
                    server,
                    port,
                    tls
                )

                logging.info('Email enviado correctamente.')

            except Exception as e:
                #raise e
                logging.error("Al Enviar email: {}.".format(e))


def main():
    """Funcion Principal"""

    # Cargando variables pasadas como argumentos
    args = loading_args()
    # estableciendo la configuracion de los logs
    log_configuration(args)

    logging.debug("Inicio de modo de depuracion.")

    # Cargando variables de configuracion
    config = load_config(args.config)

    # Funcion que controla montaje de la und
    fun_mount_und(config)

    comando = copy_mirror(
        source_path=config.get("GENERAL", "source_path"),
        destiny_path=config.get("GENERAL", "destiny_path"),
        copy_options=config.get("GENERAL", "copy_options"),
        format_command=config.get("GENERAL", "format_command"),
        binary=config.get("GENERAL", "binary")
    )

    if comando:
        if not args.test:
            run_command(comando)
        else:
            logging.info(comando)
            logging.info("Se evito la ejecucion del comando por estar habilitado el modo pruebas.")

    # Funcion controla el envio de correo
    fun_send_mail(config, args)


if __name__ == '__main__':
    main()
