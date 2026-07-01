import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        os.makedirs("Logs", exist_ok=True)

        logger = logging.getLogger("LogGen")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("Logs/automation.log")

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger