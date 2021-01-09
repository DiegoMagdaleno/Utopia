# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sed(AutotoolsPackage, GNUMirrorPackage):
    """GNU implementation of the famous stream editor."""
    homepage = "http://www.gnu.org/software/sed/"
    gnu_mirror_path = "sed/sed-4.8.tar.xz"

    version('4.8', sha256='f79b0cfea71b37a8eeec8490db6c5f7ae7719c35587f21edb0617f370eeff633')
    version('4.2.2', sha256='f048d1838da284c8bc9753e4506b85a1e0cc1ea8999d36f6995bcb9460cddbd7')

    def url_for_version(self, version):

        if (version < Version('4.3')):
            self.gnu_mirror_path = self.gnu_mirror_path.replace("xz", "bz2")
        return super(Sed, self).url_for_version(version)