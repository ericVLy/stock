"""logging demo model"""

import logging

import time
import os

root_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..")
log_dir = os.path.join(root_dir,"log")


class DemoLogger():
    """ logging demo class """
    def __init__(self, log_name="log", logger_name="", log_level="info"):
        log_level_dict = {
            "info": logging.INFO,
            "error": logging.ERROR,
            "critical": logging.CRITICAL,
            "warning": logging.WARNING,
            "debug": logging.DEBUG,
        }
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建一个日志器
        self.logger = logging.getLogger(logger_name)

        # 设置日志输出的最低等级,低于当前等级则会被忽略
        self.logger.setLevel(log_level_dict[log_level])

        # 创建处理器：sh为控制台处理器，fh为文件处理器
        sh = logging.StreamHandler()

        # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
        log_file = os.path.join(log_dir,
                                f"{log_name}{time.strftime("%Y-%m-%d-%H-%M-%S",
                                                           time.localtime())}.log")
        fh = logging.FileHandler(log_file,encoding="UTF-8")

        # 创建格式器,并将sh，fh设置对应的格式
        formator = logging.Formatter(fmt="[%(asctime)s][%(filename)s]"+
                                     "[%(module)s][%(funcName)s][line:%(lineno)d]"+
                                     "[%(levelname)s]: %(message)s",
                                     datefmt="%Y/%m/%d %X")
        sh.setFormatter(formator)
        fh.setFormatter(formator)

        # 将处理器，添加至日志器中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)



# logprint = DemoLogger().logger


# if __name__ == '__main__':
#     logprint.debug("------这是debug信息---")
#     logprint.info("------这是info信息---")
#     logprint.warning("------这是warning信息---")
#     logprint.error("------这是error信息---")
#     logprint.critical("------这是critical信息---")
