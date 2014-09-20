from setuptools import setup

setup(name='KLJIchtegemSite',
      version='1.0',
      description='website voor KLJ Ichtegem',
      author='Matthias Feys',
      author_email='matthiasfeys@hotmail.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask>=0.7.2', 'MarkupSafe','Flask-SQLAlchemy==0.16','Flask-Security>=1.7.3','flask-wtf','WTForms','ics'],
     )
