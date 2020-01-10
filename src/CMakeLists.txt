project(oxygen-icons)

cmake_minimum_required(VERSION 2.6)
# include specific modules
set (CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

if (WIN32)
   set(ICON_INSTALL_DIR         "share/icons"             ) # The icon install dir (default ${SHARE_INSTALL_PREFIX}/share/icons/)
else (WIN32)
   set(SHARE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}/share" )
   set(ICON_INSTALL_DIR     "${SHARE_INSTALL_PREFIX}/icons" )
endif(WIN32)

########### install files ###############

set( oxygen_icon_dirs  8x8 16x16 22x22 32x32 48x48 64x64 128x128 256x256 )

install( DIRECTORY ${oxygen_icon_dirs} DESTINATION ${ICON_INSTALL_DIR}/oxygen PATTERN .svn EXCLUDE PATTERN "*.sh" EXCLUDE )
install( FILES index.theme DESTINATION ${ICON_INSTALL_DIR}/oxygen )

