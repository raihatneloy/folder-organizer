from setuptools import setup

setup(
    name='folder-organizer-package',
    version='0.0-dev',
    install_requires=['click'],
    packages=['folder_organizer_package'],
    entry_points = {
        'console_scripts': [
            'folder_organizer=folder_organizer_package.folder_organizer_script:main'
        ]
    }
)