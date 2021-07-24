import os
import random
import gc
from copy import deepcopy
from PIL import Image, ImageDraw    # PIP package

from triangle import Triangle

# Generated images will be 256x256 pixels
RESOLUTION = (256, 256)
NUM_TRIANGLES = 512

class GeneticAlgorithm:

    def __init__(self, image, population):

        '''Class implements methods to recreate images via triangles and a genetic 
        algorithm through asexual reproduction.
        
        :param image: The image to be replicated
        :param population: The number of children per generation
        '''

        self.generation = 0
        self.parent = []
        self.file_type = image[image.index('.'):]

        self.image = Image.open(image).resize(RESOLUTION)
        self.population = population


    def draw_first_gen(self, children):

        '''Prepares the first generation of images with their triangles.
        
        :param children: The incoming list of "blank" images to be drawn on
        :return: A list of drawn images with their respective triangles
        '''

        drawn_images = []

        for child in children:

            triangles = []

            # Allows for the image to be drawn on
            image = ImageDraw.Draw(child, 'RGBA')

            for _ in range(NUM_TRIANGLES):

                triangle = Triangle()
                triangles.append(triangle)

                image.polygon(triangle.get_edges(), fill=triangle.get_RGBA())
            
            # Children with their respective triangles are grouped together
            drawn_images.append([child, triangles])
        
        return drawn_images


    def run(self):

        '''Prepares the program to run based on user input.'''

        # Prepare the first generation
        first_gen = [(Image.new('RGB', size=RESOLUTION)) for _ in range(self.population)]
        first_gen = self.draw_first_gen(first_gen)

        self.get_fitness(first_gen)
        next_gen = self.reproduce()

        # Keeps running until an exact replica is made
        while not self.get_fitness(next_gen):

            next_gen = self.reproduce()


    def get_fitness(self, children):

        '''Calculates fitness for a generation.
        
        Fitness is the sum of the differences in pixels between the children and the
        original image. Fitness is calulated for each child and ranked based on lowest
        value (least difference).
        
        :param children: A list of images along with their respective triangles
        :return: If a replica was created or not
        '''

        for child in children:

            fitness = 0

            # Compare the pixels of the child to the original image.
            # The difference between the two is the child's fitness.
            for x in range(RESOLUTION[0]):

                for y in range(RESOLUTION[1]):

                    # Get the RGB values of pixels at the following location
                    # Recall each child contains: [image, triangles]
                    r, g, b = child[0].getpixel((x, y))
                    R, G, B = self.image.getpixel((x, y))

                    fitness += abs(R - r) + abs(G - g) + abs(B - b)
            
            # Current state: [image, triangles, fitness]
            child.append(fitness)
        
        self.parent = self.get_parent(children)

        del children
        gc.collect()

        # Check if a replica was created through fitness value
        if self.parent[2] == 0:

            print('-- Replica created --')
            return True

        return False


    def get_parent(self, children):

        '''Sorts the children by their fitness values and returns the best child.
        
        :param children: The children to be sorted by fitness value
        :return: The best child of the generation
        '''

        # Sort children by ascending value; less is better
        children.sort(reverse=False, key=lambda child: child[2])

        # Save the best image every 100 generations and print its fitness
        if self.generation % 100 == 0:

            print(f'Fitness after {self.generation} generations: {children[0][2]}')
            children[0][0].save(os.path.join('output/', 
                                             f'{self.generation}{self.file_type}'))
        
        # [image, triangles, fitness]
        return children[0]


    def reproduce(self):

        '''Asexual reproduction.
        
        The parent's triangles are taken and given the chance to mutate in an attempt
        to create better offspring.
        
        :param parent: The best image from the current generation
        :return: The new generation of images based off the parent
        '''

        offspring = [(Image.new('RGB', size=RESOLUTION)) for _ in range(self.population)]
        next_gen = []

        # Draw on each blank image
        for child in offspring:

            triangles = []
            image = ImageDraw.Draw(child, 'RGBA')

            # The child will inherit the triangles from the parent
            # Each triangle could mutate (depends on MUTATION_RATE in triangle.py)
            for triangle in self.parent[1]:

                # NEED to perform a deepcopy to create an unique triangle instance
                triangle_copy = deepcopy(triangle)

                triangle_copy.mutate_edges()
                triangle_copy.mutate_colors()

                triangles.append(triangle_copy)
                image.polygon(triangle_copy.get_edges(), fill=triangle_copy.get_RGBA())
            
            next_gen.append([child, triangles])
        
        self.generation += 1

        # Conserve memory as much as possible for long runs
        del triangles
        del offspring

        gc.collect()

        return next_gen