import logging
import logging.config
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
import yaml
import os


def try_console_and_file():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler('try_logging.log')
    file_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger(__name__)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug('debug_log')
    logger.info('info_log')
    logger.warning('warning_log')
    logger.error('error_log')
    logger.critical('critical_log')


def _load_yaml_conf():
    yaml_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logging.yaml')
    with open(yaml_path) as f:
        return yaml.load(f)


def log_all_levels(logger):
    logger.debug('debug_log')
    logger.info('info_log')
    logger.warning('warning_log')
    logger.error('error_log')
    logger.critical('critical_log')


def try_yaml_conf():
    # logger = logging.getLogger(__name__)
    # logger = logging.getLogger('root')
    # print(conf)
    # print(logger.handlers)
    # print(logger.level)

    # print(logging._handlers)
    # print(logging.config.)
    logger = create_yaml_logger()
    log_all_levels(logger)


def create_yaml_logger():
    conf = _load_yaml_conf()
    logging.config.dictConfig(conf)
    logger_name = 'simpleExample'
    logger = logging.getLogger(logger_name)

    return logger


if __name__ == '__main__':
    try_yaml_conf()
