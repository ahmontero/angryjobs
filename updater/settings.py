# -*- encoding: utf-8 -*-

import os


class ImproperlyConfigured(Exception):pass


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

SOURCE = 'infojobs'
URL = 'http://www.infojobs.net/ofertas-trabajo/informatica-telecomunicaciones/'

WEB_URL = 'http://127.0.0.1:8000'
API = '/api/v1/'

USERNAME = get_env_variable('TE_API_USER')
API_KEY = get_env_variable('TE_API_KEY')

CONF = '/?username=%s&api_key=%s' % (USERNAME, API_KEY)


BECARIO_ANALISTA_SENIOR = 1
BECARIO_ANALISTA_JUNIOR = 2
CRAFTMAN_SENIOR = 3
CRAFTMAN_JUNIOR = 4

BAS_CAT = (
            u'analista', u'analistas', u'arquitecto', u'arquitectos',
            u'consultor', u'consultores',
            u'coordinador',
            u'director',
            u'funcional',
            u'gestión', u'gestion',
            u'hibernate',
            u'java',
            u'jefe',
            u'manager',
            u'oracle',
            u'sap',
            u'spring',
            u'urge', u'urgente',
            )

BAJ_CAT = (
            u'abap',
            u'administrador',
            u'ap',
            u'db2',
            u'formador',
            u'j2ee',
            u'php',
            u'pl/sql', u'pl-sql',
            u'responsable',
            u'senior', u'sr',
            u'titulado',
            )

CRS_CAT = (
            u'cobol',
            u'fortran',
            u'junior', u'jr',
            u'tester',
            u'testing',
            )

CRJ_CAT = (
            u'beca',
            u'programador', u'programadores',
            )

NON_SHITTY_COMPANIES = (
            u'Apple',
            u'Hewlett Packard',
            u'Softonic',
            u'Sony',
            u'Tuenti',
            )
