# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LinuxHeaders(Package):
    """The Linux kernel headers."""

    homepage = "https://www.kernel.org/"
    url      = "https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.6.tar.xz"
    list_url = "https://www.kernel.org/pub/linux/kernel"
    list_depth = 2


    version('5.10.6', sha256='7767d02c1cb5eb2a8d3c2b15a3f93e85b98baa6e9d93a3b9e3ec0e959d0a690b')
    version('4.9.10', sha256='bd6e05476fd8d9ea4945e11598d87bc97806bbc8d03556abbaaf809707661525')

    def setup_build_environment(self, env):
        # This variable is used in the Makefile. If it is defined on the
        # system, it can break the build if there is no build recipe for
        # that specific ARCH
        env.unset('ARCH')

    def install(self, spec, prefix):
        make('headers_install', 'INSTALL_HDR_PATH={0}'.format(prefix))
    
    def url_for_version(self, version):
        url = "https://cdn.kernel.org/pub/linux/kernel/v{0}.x/linux-{1}.tar.xz"
        subdir = version.up_to(2)
        major = version.up_to(1)
        if int(str(major)) > 2:
            subdir = major 
        return url.format(subdir, version)