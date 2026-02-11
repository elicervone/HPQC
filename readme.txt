allora

innanzitutto da powershell windows: wsl -d Ubuntu-22.04
entro nella cartella:   (base) elisa@AF:/$ cd home/
                        (base) elisa@AF:/home$ cd elisa/
                        (base) elisa@AF:~$ cd HPQC/
                        (base) elisa@AF:~/HPQC$

*** per scrivere i file di codice su vsc devo fare "ctrl+shift+p" e poi premere "connect to wsl" e poi aprire semplicemente la cartella HPQC

ho aggiunto i comandi per compilare all'interno dei file c++

--- per usare python: conda activate cuq
    per compilare ed eseguire si fa solo python ./file.py

    MA FORSE PER PYTHON NON CI STA CUSTABILIZER (O ALMENO IO NON LO TENGO E NON FUNZIONA)

    per uscire dall'ambiente virtuale: conda deactivate

miniconda contiene le seguenti cartelle:
(***base***) elisa@AF:~/miniconda3$ ls
LICENSE.txt  compiler_compat  condarc.d  include  man   sbin   ssl          uninstall.sh
_conda       conda-meta       envs       lib      nvvm  share  targets      x86_64-conda-linux-gnu
bin          condabin         etc        libexec  pkgs  shell  test_cuq.py

in include saranno contenuti tutti i moduli che possiamo includere:
(base) elisa@AF:~/miniconda3/include$ ls
GL                 default.h              libssh2.h            sqlite3.h          tkDList.h            tkUnixDefault.h
X11                eti.h                  libssh2_publickey.h  sqlite3ext.h       tkDecls.h            tkUnixInt.h
archive.h          etip.h                 libssh2_sftp.h       tcl.h              tkEntry.h            tkUnixPort.h
archive_entry.h    ev++.h                 libxml2              tclDecls.h         tkFileFilter.h       tkUuid.h
ares.h             ev.h                   localcharset.h       tclInt.h           tkFont.h             tl
ares_build.h       expat.h                lz4.h                tclIntDecls.h      tkImgPhoto.h         unctrl.h
ares_dns.h         expat_config.h         lz4frame.h           tclIntPlatDecls.h  tkInt.h              unicase.h
ares_dns_record.h  expat_external.h       lz4frame_static.h    tclOO.h            tkIntDecls.h         unicode
ares_nameser.h     fakemysql.h            lz4hc.h              tclOODecls.h       tkIntPlatDecls.h     uniconv.h
ares_version.h     fakepq.h               lzma                 tclOOInt.h         tkIntXlibDecls.h     unictype.h
autosprintf.h      fakesql.h              lzma.h               tclOOIntDecls.h    tkMacOSX.h           unigbrk.h
bzlib.h            ffi.h                  mamba                tclPlatDecls.h     tkMacOSXColor.h      unilbrk.h
cudensitymat.h     ffitarget.h            menu.h               tclPort.h          tkMacOSXConstants.h  unimetadata.h
cupauliprop.h      fmt                    mysqlStubs.h         tclThread.h        tkMacOSXCursors.h    uniname.h
curl               form.h                 ncurses              tclTomMath.h       tkMacOSXDebug.h      uninorm.h
curses.h           gettext-po.h           ncurses.h            tclTomMathDecls.h  tkMacOSXDefault.h    unistdio.h
cursesapp.h        gmock                  ncurses_dll.h        tclUnixPort.h      tkMacOSXEvent.h      unistr.h
cursesf.h          gtest                  ncursesw             tdbc.h             tkMacOSXFont.h       unistring
cursesm.h          iconv.h                nghttp2              tdbcDecls.h        tkMacOSXInt.h        unitypes.h
cursesp.h          idn2.h                 nlohmann             tdbcInt.h          tkMacOSXKeysyms.h    uniwbrk.h
cursesw.h          infiniband             odbcStubs.h          term.h             tkMacOSXPort.h       uniwidth.h
cursslk.h          itcl.h                 openssl              term_entry.h       tkMacOSXPrivate.h    uuid
***custabilizer.h     itcl2TclOO.h           panel.h              termcap.h          tkMacOSXWm.h         xcb
***custabilizer.hpp   itclDecls.h            pcre2.h              test_data.hpp      tkMacOSXXCursors.h   yaml-cpp
custatevec.h       itclInt.h              pcre2posix.h         textstyle          tkMenu.h             zconf.h
cutensor           itclIntDecls.h         pqStubs.h            textstyle.h        tkMenubutton.h       zdict.h
cutensor.h         itclMigrate2TclCore.h  python3.13           tk.h               tkPlatDecls.h        zlib.h
cutensorMg.h       itclTclIntStubsFcn.h   rdma                 tk3d.h             tkPort.h             zstd.h
cutensorMp         jansson.h              readline             tkArray.h          tkScale.h            zstd_errors.h
cutensorMp.h       jansson_config.h       reproc               tkBusy.h           tkScrollbar.h
cutensornet        ks_names.h             reproc++             tkButton.h         tkSelect.h
cutensornet.h      libcharset.h           simdjson.h           tkCanvas.h         tkText.h
dbus-1.0           libnl3                 solv                 tkColor.h          tkUndo.h

in lib saranno contenute tutte le librerie che possiamo linkare:
(base) elisa@AF:~/miniconda3/lib$ ls
cmake                           libform.so.6              libncursesw.so                 libtkstub8.6.a
dbus-1.0                        libform.so.6.5            libncursesw.so.6               libunistring.so
engines-3                       libformw.a                libncursesw.so.6.5             libunistring.so.5
gettext                         libformw.so               libnghttp2.so                  libunistring.so.5.2.0
ibacm                           libformw.so.6             libnghttp2.so.14               libuuid.a
icu                             libformw.so.6.5           libnghttp2.so.14.29.1          libuuid.so
itcl4.3.0                       libgcc_s.so               libnl                          libuuid.so.1
libX11-xcb.so                   libgcc_s.so.1             libnl-3.a                      libuuid.so.1.3.0
libX11-xcb.so.1                 libgettextlib-0.21.so     libnl-3.so                     libxcb-composite.so
libX11-xcb.so.1.0.0             libgettextlib.so          libnl-3.so.200                 libxcb-composite.so.0
libX11.so                       libgettextpo.a            libnl-3.so.200.26.0            libxcb-composite.so.0.0.0
libX11.so.6                     libgettextpo.so           libnl-cli-3.a                  libxcb-damage.so
libX11.so.6.4.0                 libgettextpo.so.0         libnl-cli-3.so                 libxcb-damage.so.0
libXau.so                       libgettextpo.so.0.5.7     libnl-cli-3.so.200             libxcb-damage.so.0.0.0
libXau.so.6                     libgettextsrc-0.21.so     libnl-cli-3.so.200.26.0        libxcb-dbe.so
libXau.so.6.0.0                 libgettextsrc.so          libnl-genl-3.a                 libxcb-dbe.so.0
libXdmcp.so                     libgfortran.so            libnl-genl-3.so                libxcb-dbe.so.0.0.0
libXdmcp.so.6                   libgfortran.so.5          libnl-genl-3.so.200            libxcb-dpms.so
libXdmcp.so.6.0.0               libgfortran.so.5.0.0      libnl-genl-3.so.200.26.0       libxcb-dpms.so.0
libarchive.a                    libgmock.so               libnl-idiag-3.a                libxcb-dpms.so.0.0.0
libarchive.so                   libgmock.so.1.11.0        libnl-idiag-3.so               libxcb-dri2.so
libarchive.so.13                libgmock_main.so          libnl-idiag-3.so.200           libxcb-dri2.so.0
libarchive.so.13.8.2            libgmock_main.so.1.11.0   libnl-idiag-3.so.200.26.0      libxcb-dri2.so.0.0.0
libasprintf.a                   libgomp.so                libnl-nf-3.a                   libxcb-dri3.so
libasprintf.so                  libgomp.so.1              libnl-nf-3.so                  libxcb-dri3.so.0
libasprintf.so.0                libgomp.so.1.0.0          libnl-nf-3.so.200              libxcb-dri3.so.0.1.0
libasprintf.so.0.0.0            libgtest.so               libnl-nf-3.so.200.26.0         libxcb-glx.so
libatomic.so                    libgtest.so.1.11.0        libnl-route-3.a                libxcb-glx.so.0
libatomic.so.1                  libgtest_main.so          libnl-route-3.so               libxcb-glx.so.0.0.0
libatomic.so.1.2.0              libgtest_main.so.1.11.0   libnl-route-3.so.200           libxcb-present.so
libblas.so                      libhistory.a              libnl-route-3.so.200.26.0      libxcb-present.so.0
libbz2.a                        libhistory.so             libnl-xfrm-3.a                 libxcb-present.so.0.0.0
libbz2.so                       libhistory.so.8           libnl-xfrm-3.so                libxcb-randr.so
libbz2.so.1.0                   libhistory.so.8.3         libnl-xfrm-3.so.200            libxcb-randr.so.0
libbz2.so.1.0.8                 libhns.so                 libnl-xfrm-3.so.200.26.0       libxcb-randr.so.0.1.0
libcares.so                     libhns.so.1               libnvJitLink.so.13             libxcb-record.so
libcares.so.2                   libhns.so.1.0.60.0        libnvJitLink.so.13.1.115       libxcb-record.so.0
libcares.so.2.19.4              libibmad.so               libnvblas.so.13                libxcb-record.so.0.0.0
libcblas.so                     libibmad.so.5             libnvblas.so.13.2.1.1          libxcb-render.so
libcharset.a                    libibmad.so.5.5.60.0      libnvrtc-builtins.so.13.1      libxcb-render.so.0
libcharset.so                   libibnetdisc.so           libnvrtc-builtins.so.13.1.115  libxcb-render.so.0.0.0
libcharset.so.1                 libibnetdisc.so.5         libnvrtc.so.13                 libxcb-res.so
libcharset.so.1.0.0             libibnetdisc.so.5.1.60.0  libnvrtc.so.13.1.115           libxcb-res.so.0
libcrypto.a                     libibumad.so              libopenblas.so                 libxcb-res.so.0.0.0
libcrypto.so                    libibumad.so.3            libopenblas.so.0               libxcb-screensaver.so
libcrypto.so.3                  libibumad.so.3.4.60.0     libopenblasp-r0.3.31.so        libxcb-screensaver.so.0
libcublas.so.13                 libibverbs                libpanel.a                     libxcb-screensaver.so.0.0.0
libcublas.so.13.2.1.1           libibverbs.so             libpanel.so                    libxcb-shape.so
libcublasLt.so.13               libibverbs.so.1           libpanel.so.6                  libxcb-shape.so.0
libcublasLt.so.13.2.1.1         libibverbs.so.1.15.60.0   libpanel.so.6.5                libxcb-shape.so.0.0.0
libcudart.so.13                 libiconv.a                libpanelw.a                    libxcb-shm.so
libcudart.so.13.1.80            libiconv.so               libpanelw.so                   libxcb-shm.so.0
libcudensitymat.so              libiconv.so.2             libpanelw.so.6                 libxcb-shm.so.0.0.0
libcudensitymat.so.0            libiconv.so.2.6.1         libpanelw.so.6.5               libxcb-sync.so
libcudensitymat.so.0.4.0.4      libicudata.a              libpcre2-16.a                  libxcb-sync.so.1
libcudss.so.0                   libicudata.so             libpcre2-16.so                 libxcb-sync.so.1.0.0
libcudss.so.0.7.1               libicudata.so.73          libpcre2-16.so.0               libxcb-xf86dri.so
libcudss_mtlayer_gomp.so.0      libicudata.so.73.1        libpcre2-16.so.0.14.0          libxcb-xf86dri.so.0
libcudss_mtlayer_gomp.so.0.7.1  libicui18n.a              libpcre2-32.a                  libxcb-xf86dri.so.0.0.0
libcufft.so.12                  libicui18n.so             libpcre2-32.so                 libxcb-xfixes.so
libcufft.so.12.1.0.78           libicui18n.so.73          libpcre2-32.so.0               libxcb-xfixes.so.0
libcufftw.so.12                 libicui18n.so.73.1        libpcre2-32.so.0.14.0          libxcb-xfixes.so.0.0.0
libcufftw.so.12.1.0.78          libicuio.a                libpcre2-8.a                   libxcb-xinerama.so
libcufile.so.0                  libicuio.so               libpcre2-8.so                  libxcb-xinerama.so.0
libcufile.so.1.16.1             libicuio.so.73            libpcre2-8.so.0                libxcb-xinerama.so.0.0.0
libcufile_rdma.so.1             libicuio.so.73.1          libpcre2-8.so.0.14.0           libxcb-xinput.so
libcufile_rdma.so.1.16.1        libicutest.a              libpcre2-posix.a               libxcb-xinput.so.0
libcupauliprop.so               libicutest.so             libpcre2-posix.so              libxcb-xinput.so.0.1.0
libcupauliprop.so.0             libicutest.so.73          libpcre2-posix.so.3            libxcb-xkb.so
libcupauliprop.so.0.2.0.4       libicutest.so.73.1        libpcre2-posix.so.3.0.6        libxcb-xkb.so.1
libcurand.so.10                 libicutu.a                libpython3.13.so               libxcb-xkb.so.1.0.0
libcurand.so.10.4.1.81          libicutu.so               libpython3.13.so.1.0           libxcb-xlib.so.0
libcurl.so                      libicutu.so.73            libpython3.so                  libxcb-xlib.so.0.0.0
libcurl.so.4                    libicutu.so.73.1          libquadmath.so                 libxcb-xtest.so
libcurl.so.4.8.0                libicuuc.a                libquadmath.so.0               libxcb-xtest.so.0
libcusolver.so.12               libicuuc.so               libquadmath.so.0.0.0           libxcb-xtest.so.0.0.0
libcusolver.so.12.0.9.81        libicuuc.so.73            librdmacm.so                   libxcb-xv.so
libcusolverMg.so.12             libicuuc.so.73.1          librdmacm.so.1                 libxcb-xv.so.0
libcusolverMg.so.12.0.9.81      libidn2.so                librdmacm.so.1.4.60.0          libxcb-xv.so.0.0.0
libcusparse.so.12               libidn2.so.0              libreadline.a                  libxcb-xvmc.so
libcusparse.so.12.7.3.1         libidn2.so.0.4.0          libreadline.so                 libxcb-xvmc.so.0
***libcustabilizer.so              libitm.so                 libreadline.so.8               libxcb-xvmc.so.0.0.0
***libcustabilizer.so.0            libitm.so.1               libreadline.so.8.3             libxcb.so
***libcustabilizer.so.0.2.0.4      libitm.so.1.0.0           libreproc++.so                 libxcb.so.1
libcustatevec.so                libjansson.so             libreproc++.so.14              libxcb.so.1.1.0
libcustatevec.so.1              libjansson.so.4           libreproc++.so.14.2.4          libxml2.so
libcustatevec.so.1.12.0.4       libjansson.so.4.14.0      libreproc.so                   libxml2.so.2
libcutensor.so                  liblapack.so              libreproc.so.14                libxml2.so.2.13.9
libcutensor.so.2                liblz4.so                 libreproc.so.14.2.4            libyaml-cpp.so
libcutensor.so.2.4.1            liblz4.so.1               libsimdjson.so                 libyaml-cpp.so.0.8
libcutensorMg.so                liblz4.so.1.9.4           libsimdjson.so.23              libyaml-cpp.so.0.8.0
libcutensorMg.so.2              liblzma.so                libsimdjson.so.23.0.0          libz.a
libcutensorMg.so.2.4.1          liblzma.so.5              libsolv.so                     libz.so
libcutensorMp.so                liblzma.so.5.6.4          libsolv.so.1                   libz.so.1
libcutensorMp.so.2              libmamba.so               libsolvext.so                  libz.so.1.3.1
libcutensorMp.so.2.4.1          libmamba.so.4             libsolvext.so.1                libzstd.a
libcutensornet.so               libmamba.so.4.0.1         libsqlite3.so                  libzstd.so
libcutensornet.so.2             libmana.so                libsqlite3.so.0                libzstd.so.1
libcutensornet.so.2.11.0.4      libmana.so.1              libsqlite3.so.3.51.0           libzstd.so.1.5.7
libdbus-1.so                    libmana.so.1.0.60.0       libssh2.so                     ossl-modules
libdbus-1.so.3                  libmenu.a                 libssh2.so.1                   pkgconfig
libdbus-1.so.3.38.3             libmenu.so                libssh2.so.1.0.1               preloadable_libintl.so
libefa.so                       libmenu.so.6              libssl.a                       python3.13
libefa.so.1                     libmenu.so.6.5            libssl.so                      rsocket
libefa.so.1.4.60.0              libmenuw.a                libssl.so.3                    sqlite3.45.3
libev.so                        libmenuw.so               libstdc++.so                   stubs
libev.so.4                      libmenuw.so.6             libstdc++.so.6                 systemd
libev.so.4.0.0                  libmenuw.so.6.5           libstdc++.so.6.0.34            tcl8
libexpat.so                     libmlx4.so                libtcl8.6.so                   tcl8.6
libexpat.so.1                   libmlx4.so.1              libtclstub8.6.a                tclConfig.sh
libexpat.so.1.11.1              libmlx4.so.1.0.60.0       libtextstyle.a                 tclooConfig.sh
libffi.7.so                     libmlx5.so                libtextstyle.so                tdbc1.1.9
libffi.8.so                     libmlx5.so.1              libtextstyle.so.0              tdbcmysql1.1.9
libffi.a                        libmlx5.so.1.25.60.0      libtextstyle.so.0.1.1          tdbcodbc1.1.9
libffi.so                       libmpdec.so.4             libtinfo.a                     tdbcpostgres1.1.9
libffi.so.7                     libmpdec.so.4.0.0         libtinfo.so                    terminfo
libffi.so.8                     libncurses++.a            libtinfo.so.6                  thread2.8.10
libffi.so.8.1.2                 libncurses++w.a           libtinfo.so.6.5                tk8.6
libfmt.so                       libncurses.a              libtinfow.a                    tkConfig.sh
libfmt.so.11                    libncurses.so             libtinfow.so                   udev
libfmt.so.11.2.0                libncurses.so.6           libtinfow.so.6
libform.a                       libncurses.so.6.5         libtinfow.so.6.5
libform.so                      libncursesw.a             libtk8.6.so