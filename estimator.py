import pickle
import numpy as np
from Estimator.factory import Factory
import argparse


def parsing_arguments():
    parser = argparse.ArgumentParser(description='Synthetic data generation')
    parser.add_argument('-i', '--input', type=str, help='Path to input file (output of Generator',
                        default="generated_shapes.pkl")
    parser.add_argument('-o', '--output', type=str, help='Path to output file', default="estimated_shapes.pkl")
    parser.add_argument('-it', '--iterations', type=int, help='number of iterations', default=500)
    parser.add_argument('-g', '--debug', action='store_true', help='Run debug mode')
    return vars(parser.parse_args())


def extract_data(points):
    return np.array([p[0] for p in points]), np.array([p[1] for p in points])


def main():
    with open(args.get("input"), 'rb') as source:
        f = pickle.load(source)
    debug_mode = args.get("debug")
    output_path = args.get("output")
    fac = Factory()
    shapes = []
    for shape in f:
        p = shape.points
        x_data, y_data = (extract_data(p))
        ransac = fac.creation(type(shape).__name__, x_data, y_data, 500)
        ransac.execute_estimator()
        if debug_mode:
            ransac.plot()
        shapes.append(shape)

    with open(output_path, 'wb') as f:
        pickle.dump(ransac, f)


if __name__ == '__main__':
    args = parsing_arguments()
    main()
