import random

# 5% chance to mutate. Change to your likings
MUTATION_RATE = 0.05

class Triangle:

    def __init__(self):

        '''Class defines a triangle's RGBA values and edge locations. Additional methods 
        are implemented to mutate a triangle's attributes.
        '''

        # Triangles are in RGBA format
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.a = random.randint(95, 115)

        self.edge1 = [random.randint(0, 255), random.randint(0, 255)]
        self.edge2 = [random.randint(0, 255), random.randint(0, 255)]
        self.edge3 = [random.randint(0, 255), random.randint(0, 255)]

    
    def get_edges(self):

        '''Getter method that makes it easy to input the edge coordinates into the 
        `ImageDraw.Draw.polygon()` method.
        
        :return: The coordinates of each edge in a list
        '''

        return [(self.edge1[0], self.edge1[1]),
                (self.edge2[0], self.edge2[1]),
                (self.edge3[0], self.edge3[1])]
        
    
    def get_RGBA(self):

        '''Getter method that makes it easy to input the RGBA values into the 
        `ImageDraw.Draw.polygon()` method.
        
        :return: The RGBA value of the triangle packed in a tuple
        '''

        return self.r, self.g, self.b, self.a
    

    def mutate_colors(self):

        '''Mutates color and transparency by a small amount.'''

        if MUTATION_RATE > random.random():

            self.r = max(0, min(self.r + random.randint(-10, 10), 255))
            self.g = max(0, min(self.g + random.randint(-10, 10), 255))
            self.b = max(0, min(self.b + random.randint(-10, 10), 255))
            self.a = max(95, min(self.a + random.randint(-5, 5), 115))


    def mutate_edges(self):

        '''Mutates edge positions by a small amount.'''

        if MUTATION_RATE > random.random():

            self.edge1[0] = max(0, min(255, self.edge1[0] + random.randint(-20, 20)))
            self.edge1[1] = max(0, min(255, self.edge1[1] + random.randint(-20, 20)))

            self.edge2[0] = max(0, min(255, self.edge2[0] + random.randint(-20, 20)))
            self.edge2[1] = max(0, min(255, self.edge2[1] + random.randint(-20, 20)))

            self.edge3[0] = max(0, min(255, self.edge3[0] + random.randint(-20, 20)))
            self.edge3[1] = max(0, min(255, self.edge3[1] + random.randint(-20, 20)))