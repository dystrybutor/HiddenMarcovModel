from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument("-b", "--biased", dest="biased_probabilities",
                        help="biased dice", type=float, required=True, nargs='+')

    parser.add_argument("-pfb", "--fair_to_biased", dest="fair_to_biased",
                        help="probability from fair to biased", type=float, required=True)

    parser.add_argument("-pbf", "--biased_to_fair", dest="biased_to_fair",
                        help="probability from fair to biased", type=float, required=True)

    parser.add_argument("-n", "--number_of_throws", dest="number_of_throws",
                        help="number of dice throws", type=int, required=True)

    parser.add_argument("-t", "--algorithm_type", dest="algorithm_type",
                        help="algorithm type", type=str, required=True)

    return parser