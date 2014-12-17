from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument("-b", "--bribed", dest="bribed_sides_probabilities",
                        help="bribed dice", type=float, required=True, nargs='+')

    parser.add_argument("-pfb", "--fair_to_bribed", dest="fair_to_bribed",
                        help="probability from fair to bribed", type=float, required=True)

    parser.add_argument("-pbf", "--bribed_to_fair", dest="bribed_to_fair",
                        help="probability from fair to bribed", type=float, required=True)

    parser.add_argument("-n", "--number_of_throws", dest="number_of_throws",
                        help="number of dice throws", type=int, required=True)

    parser.add_argument("-t", "--algorithm_type", dest="algorithm_type",
                        help="algorithm type", type=str, required=True)

    return parser