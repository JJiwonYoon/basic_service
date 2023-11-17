from setuptools import find_packages, setup

package_name = 'basic_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cwsfa',
    maintainer_email='wldnjs0488@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'basic_client = ' + package_name + '.basic_client:main',
        'basic_server = ' + package_name + '.basic_server:main',
        ],
    },
)
