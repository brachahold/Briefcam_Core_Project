import pickle
from Tester.factory import Factory
from Tester.geo_tester import GeoTester
import argparse


def parsing_arguments():
    parser = argparse.ArgumentParser(description='Synthetic data generation')
    parser.add_argument('-gt', '--gt_input_path', type=str, help="Ground truth input file (output of generator)",
                        default="generated_shapes.pkl")
    parser.add_argument('-est', '--est_input_path', type=str, help='Estimated model input file (output of estimator)',
                        default="estimated_shapes.pkl")
    parser.add_argument('-g', '--debug', action='store_true', help='Run debug mode')
    return vars(parser.parse_args())


def main():
    with open(args.get("gt_input_path"), 'rb') as source:
        gt_input = pickle.load(source)
    with open(args.get("est_input_path"), 'rb') as source:
        est_input = pickle.load(source)
    debug_mode = args.get("debug")
    fac = Factory()
    shapes = []
    for i in range(len(gt_input)):
        test = fac.creation(type(gt_input[i]).__name__, gt_input[i], est_input[i])
        print(test)
        shapes.append(test)
        if debug_mode:
            test.plot([p[0] for p in gt_input[i].points], [p[1] for p in gt_input[i].points])
    print("final score:", GeoTester.get_general_score(shapes))


if __name__ == '__main__':
    args = parsing_arguments()
    main()
