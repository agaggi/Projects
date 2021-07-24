import sys
import os
import glob

from genetic import GeneticAlgorithm

def input_check(image, population):

    '''Checks the arguments entered by the user.
    
    :param image: The selected name to look for in the `images` directory
    :param population: Population size
    :return: If any errors occurred
    '''

    errors = False

    if not os.path.exists(image):

        print(f'File does not exist: {image}')
        errors = True
    
    if population < 1:

        print('Asexual reproduction requires at least one parent.')
        errors = True

    return errors


def main():

    '''Initializes the program.'''

    # Passed-in arguments
    image_path = f'images/{sys.argv[1]}'
    population = int(sys.argv[2])

    errors = input_check(image_path, population)

    if not errors:

        # Create the output folder if it does not exist
        if not os.path.exists('output'):

            os.makedirs('output')

        # Clear output from previous run
        folder = glob.glob('output/*')
        
        for image in folder:

            os.remove(image)

        algorithm = GeneticAlgorithm(image_path, population)
        algorithm.run()


if __name__ == '__main__':

    main()