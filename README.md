# Recreating Images with Triangles

This program was an assignment for *CS 580 - Introduction to Artificial Intelligence* at *Old Dominion University* during the Fall 2020 semester.

Images within the `images` directory are re-created by using triangles of various colors and transparency through the use of a genetic algorithm using asexual reproduction. Images created are compared to the original and the difference in pixels is calculated. The best image of the generation is the parent of the next.

## Execution

### Dependencies

- Python 3.7+ preferred
- [Pillow](https://pypi.org/project/Pillow/) PIP package

The program should be ran following the following format:

```bash
# Unix-based
python3 main.py {image} {population size per generation}

# Windows
py .\main.py {image} {population size per generation}
```

For example, there is a file called `apple.jpg` in the `images` directory:

```bash
python3 main.py apple.jpg 100
```

## Samples

All samples are located in the `samples` directory. Samples were given 2-4 days to run and log files are provided. Images are named after their generation. 

The setting for each of the samples are provided below:

| Image     | Population per Generation | # of Triangles | Mutation Rate |
| :-------: | :-----------------------: | :------------: | :-----------: |
| flag.jpg  | 100                       | 256            | 5%            |
| apple.jpg | 200                       | 512            | 7.5%          |
| odu.webp  | 500                       | 512            | 5%            |

**Note**: The number of triangles and mutation rate can be modified by changing the constant variables at the top of `genetic.py` and `triangle.py`.