import logging
import sys

def setup_logger(file_name):
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(f"{file_name}")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        stream_formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    return logger
