import logging
from CMDParser import create_parser
from MethodsFactory import MethodsFactory

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
    rolls, result = None, None
    if args.algorithm_type == "viterbi":
        viterbi = MethodsFactory.create_viterbi(args.biased_probabilities, args.fair_to_biased, args.biased_to_fair,
                                                args.number_of_throws)

        rolls, result =viterbi.run_test()
    elif args.algorithm_type == "aposteriori":
        aposteriori = MethodsFactory.create_aposteriori(args.biased_probabilities, args.fair_to_biased,
                                                        args.biased_to_fair, args.number_of_throws)

        rolls, result = aposteriori.run_test()

    print("{0:20s}{1:20s}{2:20s}{3:20s}".format("Dice Type", "Roll Value", "nie wiem co to", "a co to?"))

    for i in range(args.number_of_throws):
        roll = rolls[i]
        print("{0:20s}{1:20d}{2:20f}{3:20f}".format(roll.dice_type, roll.roll_value, result[0][i], result[1][i]))

if __name__ == '__main__':
    main()