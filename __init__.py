from collections import __main__
import logging
from CMDParser import create_parser

logger = logging.getLogger(__name__)
# ################################################# LOGGER CONFIGURATION #################################################
#
# LOG_FILE     = 'casino.log'
# FILEMODE     = 'a'
# MAX_BYTES    = 1048576
# BACKUP_COUNT = 20
# LEVEL        = logging.DEBUG
#
# FORMAT = '%(asctime)-15s %(levelname)8s %(process)5d %(thread)6d %(name)-25s %(filename)20s:%(lineno)-6s %(message)s'
#
# root_logger_file_handler = logging._handlers.RotatingFileHandler(filename=LOG_FILE,
#                                                                 mode=FILEMODE,
#                                                                 maxBytes=MAX_BYTES,
#                                                                 backupCount=BACKUP_COUNT)
# root_logger_formatter = logging.Formatter(fmt=FORMAT, datefmt=None)
# root_logger_file_handler.setFormatter(root_logger_formatter)
#
# root_logger = logging.getLogger()
# root_logger.addHandler(root_logger_file_handler)
# root_logger.setLevel(LEVEL)
# ########################################################################################################################


def main():
    parser = create_parser()

    args = parser.parse_args()

    if args.algorithm_type == "verbati":
        print(args)
    elif args.algorithm_type == "aposteriori":
        print(args)

if __name__ == '__main__':
    main()