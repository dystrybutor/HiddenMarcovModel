import logging
from CMDParser import create_parser
from MethodsFactory import MethodsFactory
from dice_types import DiceTypes

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
# mode=FILEMODE,
# maxBytes=MAX_BYTES,
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

    if args.algorithm_type == "viterbi":
        viterbi = MethodsFactory.create_viterbi(args.bribed_sides_probabilities, args.fair_to_bribed,
                                                args.bribed_to_fair,
                                                args.number_of_throws)

        rolls, result = viterbi.run_test()

        print("{0:20s}{1:20s}{2:30s}\n".format("Roll Value", "Thrown Dice Type", "Predicted Dice Type"))

        success = 0
        for i in range(args.number_of_throws):
            roll = rolls[i]
            if roll.dice_type == result[i]:
                success += 1
            print("{0:20s}{1:20s}{2:40s}".format(str(roll.roll_value), roll.dice_type, result[i]))

        print("\nEffectiveness {}".format(success / args.number_of_throws))

    elif args.algorithm_type == "aposteriori":
        aposteriori = MethodsFactory.create_aposteriori(args.bribed_sides_probabilities, args.fair_to_bribed,
                                                        args.bribed_to_fair, args.number_of_throws)

        rolls, result = aposteriori.run_test()

        print("{0:20s}{1:30s}{2:20s}{3:40s}{4:40s}\n".format("Thrown Dice Type", "Predicted Dice Type", "Roll Value",
                                                             "Fair Dice Prob.", "Bribed Dice Prob."))

        success = 0

        for i in range(args.number_of_throws):
            roll = rolls[i]
            predicted_dice_type = DiceTypes.FAIR if result[0][i] >= 0.5 else DiceTypes.BRIBED
            if roll.dice_type == predicted_dice_type:
                success += 1

            print("{0:20s}{1:30s}{2:20s}{3:40s}{4:40s}".format(roll.dice_type, predicted_dice_type,
                                                               str(roll.roll_value), str(result[0][i]),
                                                               str(result[1][i])))

        print("\nEffectiveness {}".format(success / args.number_of_throws))


if __name__ == '__main__':
    main()