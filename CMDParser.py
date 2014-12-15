from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument("-fn", "--file_name", dest="file_name",
                        help="filename.* - csv and html are supported extensions", type=str, required=True)

    parser.add_argument("-f", "--folder", dest="folder_path",
                        help="test set folder", type=str, default=r'Root\ContinuousTests\BasicScope')

    parser.add_argument("-lr", "--last_runs", dest="last_runs",
                        help="number of runs", type=int, default=1)

    parser.add_argument("-ts", "--test_set_name", dest="test_set_name",
                        help="test set name", type=str, default=None)

    parser.add_argument("-p", "--project", dest="project_name",
                        help="QC project name", type=str, default="KondorPlus")

    return parser