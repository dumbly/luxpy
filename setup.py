# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
  name = 'luxpy',
  packages = find_packages(), 
  version = '1.10.0',
  license = 'GPLv3',
  description = 'Python package for lighting and color science',
  author = 'Kevin A.G. Smet',
  author_email = 'ksmet1977@gmail.com',
  url = 'https://github.com/ksmet1977/luxpy',
  download_url = 'https://github.com/ksmet1977/luxpy/archive/1.10.0.tar.gz',
  keywords = ['color', 'color appearance', 'colorimetry','photometry','CIE','color perception','lighting','color rendering','IES'], 
  install_requires=[
        'numpy',
		'scipy',
		'matplotlib',
		'pandas',
        'imageio',
        'scikit-learn',
      ],
#   package_data={'': ['luxpy/data/*.dat',
# 						  'luxpy/data/*.txt',
# 						  'luxpy/data/*.csv',
# 						  'luxpy/data/cmfs/*.dat',
# 						  'luxpy/data/cmfs/*.csv',
#                           'luxpy/data/cmfs/*.txt',
#                           'luxpy/data/cctluts/*.pkl',
#                           'luxpy/data/cctluts/*.pkl.gz',
#                           'luxpy/data/cctluts/legacy/*.dat',
# 						  'luxpy/data/cctluts/legacy/*.csv',
#                           'luxpy/data/cctluts/legacy/*.txt', 
#                           'luxpy/data/spds/*.dat',
# 						  'luxpy/data/spds/*.csv',
#                           'luxpy/data/spds/*.txt',
#                           'luxpy/data/rfls/*.dat',
# 						  'luxpy/data/rfls/*.csv',
#                           'luxpy/data/rfls/*.txt',
#                           'luxpy/data/rfls/*.npy',
#                           'luxpy/data/rfls/*.npz',
#                           'luxpy/data/rfls/*.pkl',
#                           'luxpy/data/rfls/*.pkl.gz',
#                           'luxpy/color/cct/robertson1968/luts/*.pkl',
#                           'luxpy/color/cri/iestm30/*.jfif',
#                           'luxpy/toolboxes/photbiochem/data/*.dat',
#                           'luxpy/toolboxes/photbiochem/data/*.txt',
#                           'luxpy/toolboxes/indvcmf/data/*.dat',
#                           'luxpy/toolboxes/indvcmf/data/*.txt',
#                           'luxpy/toolboxes/hypspcim/data/*.*',
#                           'luxpy/toolboxes/spectro/jeti/dll/win32/*.dll',
#                           'luxpy/toolboxes/spectro/jeti/dll/win64/*.dll',
#                           'luxpy/toolboxes/spectro/oceanoptics/data/*.dat',
#                           'luxpy/toolboxes/dispcal/data/*.csv',
#                           'luxpy/toolboxes/iolidfiles/data/*.ies',
#                           'luxpy/toolboxes/iolidfiles/data/*.ldt',
#                           'luxpy/toolboxes/sherbrooke_spectral_indices/data/*.csv',
#                           'luxpy/toolboxes/technoteamlmk/*.txt',
#                           'luxpy/toolboxes/stereoscopicviewer/harfang/assets/core/noise/*.png',
#                           'luxpy/toolboxes/stereoscopicviewer/harfang/assets/core/noise/64/*.png',
#                           'luxpy/toolboxes/stereoscopicviewer/harfang/assets/core/pbr/*.*',
#                           'luxpy/toolboxes/stereoscopicviewer/harfang/assets/core/shader/*.*',
#                           'luxpy/toolboxes/stereoscopicviewer/harfang/spheremaps/*.*'
#                           ]},
  include_package_data = True,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3',
    ],  
  python_requires='>=3.5',
)
