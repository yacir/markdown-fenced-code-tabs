
from setuptools import setup

setup(
    name='markdown-fenced-code-tabs',
    version='1.0.3',
    url='https://github.com/yacir/markdown-fenced-code-tabs',
    project_urls={
        'Bug Reports': 'https://github.com/yacir/markdown-fenced-code-tabs/issues',
        'Say Thanks!': 'http://saythanks.io/to/yacir',
        'Source': 'https://github.com/yacir/markdown-fenced-code-tabs',
    },
    packages=['markdown_fenced_code_tabs'],
    install_requires=[
        'markdown>=2.6',
        'htmlmin>=0.1.12',
        'Jinja2>=2.7.1'
    ],
    include_package_data=True,
    description='Generates a html estructure for consecutive fenced code blocks content',
    author='Yassir Barchi',
    author_email='github@yassir.fr',
    license='MIT',
    keywords=['fenced code blocks', 'code', 'fenced', 'tabs', 'mkdocs', 'markdown'],
    long_description=""" Markdown extension who generates HTML tabs for consecutive fenced code blocks in markdown syntax """,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing'
    ]
)
