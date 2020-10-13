from setuptools import setup

package_name = 'peanut2_utilities'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='peanut',
    maintainer_email='mrunaljsarvaiya@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'clock_sub = peanut2_utilities.clock_subscriber:main',
            'simple_pub = peanut2_utilities.simple_publisher:main',
        ],
    },
)
