import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # project root ka absolute path le
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(project_root, "Logs")

        os.makedirs(log_path, exist_ok=True)   # Logs folder create kar de

        logging.basicConfig(
            filename=os.path.join(log_path, "Automation.log"),
            format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
            force=True   # purana config reset
        )
        logger = logging.getLogger()
        return logger
