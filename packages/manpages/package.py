# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Manpages(MakefilePackage):
    """Describe C programming language functions, 
    important device files, and significant configuration files"""

    homepage = "https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/"
    url      = "https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-5.10.tar.xz"

    version('5.10', sha256='75102535ba119f2f223f674d84e1dcdaebf0a5ffd639b3c2e6cb0a0e34768762')

    def build(self, spec, prefix):
        make('MANDIR={0}/man'.format(prefix))
    
    def install(self, spec, prefix):
        make('install', 'MANDIR={0}/man'.format(prefix))