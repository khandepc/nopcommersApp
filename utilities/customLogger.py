import inspect
import logging

# Pavan's way
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m%d%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

#   chetan sir's way
# class LogGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger("Test_001_Login")
#
#         current_time = datetime.datetime.now().strftime("%m%d%Y %I:%M:%S %p")
#         log_path = "./Logs/automation" + current_time
#
#         handler = logging.FileHandler(log_path + ".log")
#         handler.setLevel(logging.DEBUG)
#
#         formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
#         handler.setFormatter(formatter)
#
#         logger.setLevel(level=logging.INFO)
#         logger.addHandler(handler)import logging
#         return logger

#   Rahul shetty's way
# class LogGen:
#     @staticmethod
#     def loggen():
#         #loggername = inspect.stack()[1][3]
#         logger = logging.getLogger()
#         filehandler = logging.FileHandler("./Logs/automation.log")
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
#         filehandler.setFormatter(formatter)
#         logger.addHandler(filehandler)
#         logger.setLevel(logging.INFO)
#         return logger