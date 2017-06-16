from setuptools import setup, find_packages

setup(
    name='markdown-fenced-code-tabs',
    version='0.2.0',
    url='https://github.com/yacir/markdown-fenced-code-tabs',
    py_modules=['markdown_fenced_code_tabs'],
    install_requires = ['markdown>=2.6'],
    description='Generates Bootstrap HTML Tabs for Consecutive Fenced Code Blocks',
    author='Yassir Barchi',
    author_email='yassirbarchi@gmail.com',
    license='MIT',
    keywords = ['fenced code blocks', 'code', 'tabs', 'markdown', 'mkdocs'],
    platforms='Operating System :: OS Independent',
    long_description="""This extension will convert consecutive fences blocks and convert it to HTML Bootstrap Tabs.""",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing'
    ]
)
