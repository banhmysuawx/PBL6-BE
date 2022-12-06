from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='emailHelperUtils',
  version='0.0.1',
  description='utils packages email',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='triandn',
  author_email='triandn43@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='utils_email_helper', 
  packages=find_packages(),
  install_requires=[''] 
)
