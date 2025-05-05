import logging

def setup_logger(name="ArcanApp"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("arcanapp.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
