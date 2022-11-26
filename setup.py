from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name='project_euler.util.multiples.multiples',
            sources=['project_euler/util/multiples/multiples.pyx'],
        ),
    ]
)