import setuptools



setuptools.setup(
    name='pytnn',
    version='2022.02.dev1',
    zip_safe=True,
    description='TNN Python3+ Lib',
    long_description_content_type='text/markdown',
    license='Apache License v2.0',
    author='Shi Jinghai',
    author_email='huaruhai@hotmail.com',
    url='https://github.com/shijh/py3tnn',
    install_requires=['onnx>=1.6.0'],
    python_requires='>=3.6.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
