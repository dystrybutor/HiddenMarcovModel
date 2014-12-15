from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument("-b", "--biased_dice", dest="biased_dice",
                        help="biased dice", type=str, required=True)

    parser.add_argument("-pfb", "--fair_to_biased", dest="fair_to_biased",
                        help="probability from fair to biased", type=float, required=True)

    parser.add_argument("-pbf", "--biased_to_fair", dest="biased_to_fair",
                        help="probability from fair to biased", type=float, required=True)

    parser.add_argument("-t", "--algorithm_type", dest="algorithm_type",
                        help="algorithm type", type=str, required=True)

    return parser