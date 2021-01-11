# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Glibc(AutotoolsPackage):
    """The GNU C Library is the standard system C library for all GNU systems,
    and is an important part of what makes up a GNU system.  It provides the
    system API for all programs written in C and C-compatible languages such
    as C++ and Objective C; the runtime facilities of other programming
    languages use the C library to access the underlying operating system."""

    homepage = "https://www.gnu.org/software/libc/"
    url      = "https://ftp.gnu.org/gnu/libc/glibc-2.32.tar.xz"

    version('2.32', sha256='1627ea54f5a1a8467032563393e0901077626dc66f37f10ee6363bb722222836')

    depends_on('linux-headers')

    # TODO: Add a 'test' deptype
    # depends_on('python@2.7.6:2.8,3.4.3:', type='test')
    # depends_on('py-pexpect@4.0', type='test')
    # depends_on('gdb@7.8:', type='test')

    build_directory = 'build'

    def setup_build_environment(self, env):
        env.unset('LDFLAGS')
        env.unset('LD_LIBRARY_PATH')
        env.unset('LD_RUN_PATH')
        env.unset('LIBRARY_PATH')
        env.unset('SPACK_RPATH_DIRS')
        env.unset('SPACK_LINK_DIRS')

    def configure_args(self):
        spec = self.spec
        return [
            '--disable-werror',
            '--enable-kernel=3.2',
            '--enable-stack-protector=strong',
            'libc_cv_slibdir=/lib',
            '--disable-profile',
            # Fix error: selinux/selinux.h: No such file or directory
            '--without-selinux',
            '--with-headers={0}'.format(spec['linux-headers'].prefix.include),
            '--enable-add-ons',
            '--with-tls',
            '--with-__thread',
            '--libexecdir={0}'.format(self.prefix.lib),
            'libc_cv_c_cleanup=yes',
            'libc_cv_forced_unwind=yes'
        ]

    def build(self, spec, prefix):    
        make()
    
    def install(self):
        make("install")

    @run_after('build')
    def fix_test(self):
        sed = which('sed')
        sed('-i', '/test-installation/s@$(PERL)@echo not running@', '../Makefile')

    


    
