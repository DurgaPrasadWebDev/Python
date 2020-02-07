import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.console_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler('log.log')

        self.console_format = logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s'
        )
        self.file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        self._set_console_log_format(self.console_format)
        self._set_file_log_format(self.file_format)

        self._set_console_log_handler(self.console_handler)
        self._set_file_log_handler(self.file_handler)

    def log_error(self, message: str):
        self._set_console_log_level(log_level=logging.ERROR)
        self.logger.error(message)

    def log_info(self, message: str):
        self._set_console_log_level(log_level=logging.INFO)
        self.logger.info(message)

    def log_debug(self, message: str):
        self._set_console_log_level(log_level=logging.DEBUG)
        self.logger.debug(message)

    def log_warning(self, message: str):
        self._set_console_log_level(log_level=logging.WARNING)
        self.logger.warning(message)

    def log_critical(self, message: str):
        self._set_console_log_level(log_level=logging.CRITICAL)
        self.logger.critical(message)

    def log_exception(self, message: str):
        self.logger.exception(message)

    def _set_console_log_format(self, console_format):
        self.console_handler.setFormatter(console_format)

    def _set_file_log_format(self, file_format):
        self.file_handler.setFormatter(file_format)

    def _set_console_log_handler(self, console_handler):
        self.logger.addHandler(console_handler)

    def _set_file_log_handler(self, file_handler):
        self.logger.addHandler(file_handler)
        
    def _set_file_log_level(self, log_level):
        self.file_handler.setLevel(log_level)
        
    def _set_console_log_level(self, log_level):
        self.console_handler.setLevel(log_level)
        


logger = Logger()
logger.log_error(message="hai")
logger.log_warning(message="hai")
logger.log_critical(message="hai")
try:
    a = 1/0
except Exception:
    logger.log_exception(message="hai")

