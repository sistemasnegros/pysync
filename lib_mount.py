# -*- coding: utf-8 -*-

import os

import logging


def mount_und(**kwargs):
    """list vars: , username_und, password_und, path_network, letter_und """

    username_und = kwargs.pop("username_und")
    password_und = kwargs.pop("password_und")
    path_network = kwargs.pop("path_network")
    destiny_path = kwargs.pop("destiny_path")
    letter_und = kwargs.pop("letter_und")

    comando_montar_red = "net use %s %s %s /user:%s" % (letter_und, path_network, password_und, username_und)

    if not os.path.exists(destiny_path):
        return comando_montar_red
    else:
        return
