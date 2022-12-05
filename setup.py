from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name='project_euler.util.digits.digits',
            sources=['project_euler/util/digits/digits.pyx'],
            language='c++',
        ),
        Extension(
            name='project_euler.util.multiples.multiples',
            sources=['project_euler/util/multiples/multiples.pyx'],
            language='c++',
        ),
        Extension(
            name='project_euler.util.sums.digit_factorial_sum',
            sources=['project_euler/util/sums/digit_factorial_sum.pyx'],
            language='c++',
        ),
        Extension(
            name='project_euler.util.sums.pythagorean_triplet',
            sources=['project_euler/util/sums/pythagorean_triplet.pyx'],
        ),
    ]
)