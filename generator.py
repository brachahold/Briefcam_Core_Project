import argparse
import json
from Generator.factory import Factory
import pickle


def parsing_arguments():
    parser = argparse.ArgumentParser(description='Synthetic data generation')
    parser.add_argument('-c', '--config', type=str, help='Path to config file', default="Generator/config.json")
    parser.add_argument('-o', '--output', type=str, help='Path to output file', default="generated_shapes.pkl")
    parser.add_argument('-l', '--limit', type=int, help='Measurement limit', default=10)
    parser.add_argument('-g', '--debug', action='store_true', help='Run debug mode')
    return vars(parser.parse_args())


def main():
    with open(args.get("config")) as f:
        config = json.load(f)
    num_points = config.get("num_points")
    randomness = config.get("randomness")
    limit = args.get("limit")
    debug_mode = args.get("debug")
    output_path = args.get("output")
    factory = Factory()
    shapes = [factory.creation(shape) for shape, num in config.get("shapes").items() for n in range(num)]
    for sh in shapes:
        sh.generate_noise_points(num_points, randomness, limit)
        if debug_mode:
            sh.plot()
    with open(output_path, 'wb') as f:
        pickle.dump(shapes, f)


if __name__ == '__main__':
    args = parsing_arguments()
    main()
