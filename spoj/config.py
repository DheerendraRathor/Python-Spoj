__author__ = 'dheerendra'

import ConfigParser
import utils
import lang


def set_credentials(username,password):
    config = ConfigParser.ConfigParser()
    config.read([utils.get_config_file()])
    try:
        config.add_section('user')
    except ConfigParser.DuplicateSectionError:
        pass
    config.set('user', 'username', username)
    config.set('user', 'password', utils.encode(password))
    with open(utils.get_config_file(), 'wb') as configfile:
        config.write(configfile)


def set_language(language):
    config = ConfigParser.ConfigParser()
    config.read([utils.get_config_file()])
    config.add_section('language')
    config.set('language', 'code', language)
    config.set('language', 'name', lang.LANG_DICT[int(language)])
    with open(utils.get_config_file(), 'wb') as configfile:
        config.write(configfile)