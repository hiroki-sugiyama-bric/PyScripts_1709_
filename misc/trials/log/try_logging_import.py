from .try_logging import create_yaml_logger, log_all_levels


def try_yaml_log():
    logger = create_yaml_logger()
    log_all_levels(logger)

    logger.debug('debug_log')
    logger.info('info_log')
    logger.warning('warning_log')
    logger.error('error_log')
    logger.critical('critical_log')


if __name__ == '__main__':
    pass
