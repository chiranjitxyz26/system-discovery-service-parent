#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#
Summary: Dell Inc. System Discovery Service
Name: system-discovery-service
Version: %_version
Release: %_revision
License: Commercial
Vendor: Dell Inc.
Group: System Environment/Dell Inc. Applications
URL: http://www.dell.com

#############################################################################
# rcm-fitness-common helps install OS, Consul, Vault, RabbitMQ, 
# PostGres & JDK
#############################################################################
Requires: jre = 1.8.0 rcm-fitness-common


%define _use_internal_dependency_generator 0
%define __find_requires %{nil}

%description
Dell Inc. System Discovery Service

##############################################################################
# build
##############################################################################
%build

# Creates directory if it doesn't exist
# $1: Directory path
init_dir ()
{
    [ -d $1 ] || mkdir -p $1
}

##############################################################################
# check and create the root directory
##############################################################################
init_dir ${RPM_BUILD_ROOT}/opt/dell
init_dir ${RPM_BUILD_ROOT}/opt/dell/cpsd
init_dir ${RPM_BUILD_ROOT}/opt/dell/cpsd/system-discovery-service


##############################################################################
# check and create the directories for the service
##############################################################################

SERVICE_BUILD_ROOT=${RPM_BUILD_ROOT}/opt/dell/cpsd/system-discovery-service

init_dir ${SERVICE_BUILD_ROOT}
init_dir ${SERVICE_BUILD_ROOT}/install
init_dir ${SERVICE_BUILD_ROOT}/install/dell-system-discovery-service
init_dir ${SERVICE_BUILD_ROOT}/conf
init_dir ${SERVICE_BUILD_ROOT}/image
init_dir ${SERVICE_BUILD_ROOT}/image/system-discovery-service


##############################################################################
# copy the image to the required directory
##############################################################################
cp -r ${RPM_SOURCE_DIR}/target/dependency/system-discovery-service/* ${SERVICE_BUILD_ROOT}/image/system-discovery-service


##############################################################################
# copy the scripts to the install directory
##############################################################################
echo "rpm source dir ${RPM_SOURCE_DIR}"
echo "service build dir ${SERVICE_BUILD_ROOT}"
cp -rf ${RPM_SOURCE_DIR}/build/install.sh ${SERVICE_BUILD_ROOT}/install
cp -rf ${RPM_SOURCE_DIR}/build/remove.sh ${SERVICE_BUILD_ROOT}/install
cp -rf ${RPM_SOURCE_DIR}/build/upgrade.sh ${SERVICE_BUILD_ROOT}/install
cp -riv ${RPM_SOURCE_DIR}/../system-discovery-service-distribution/build/install/.env ${SERVICE_BUILD_ROOT}/install/dell-system-discovery-service/.env


##############################################################################
# copy the unit file
##############################################################################
cp -r ${RPM_SOURCE_DIR}/target/dependency/system-discovery-service/docker-compose.yml ${SERVICE_BUILD_ROOT}/install/dell-system-discovery-service/docker-compose.yml


##############################################################################
# pre
##############################################################################
%pre
getent group dell >/dev/null || /usr/sbin/groupadd -f -r dell
getent passwd system-discovery-service >/dev/null || /usr/sbin/useradd -r -g dell -s /sbin/nologin -M system-discovery-service
exit 0


##############################################################################
# post
##############################################################################
%post
if [ $1 -eq 1 ];then
    /bin/sh /opt/dell/cpsd/system-discovery-service/install/install.sh
elif [ $1 -eq 2 ];then
    /bin/sh /opt/dell/cpsd/system-discovery-service/install/upgrade.sh
else
    echo "Unexpected argument passed to RPM %post script: [$1]"
    exit 1
fi
exit 0


##############################################################################
# preun
##############################################################################
%preun
if [ $1 -eq 0 ];then
    /bin/sh /opt/dell/cpsd/system-discovery-service/install/remove.sh
fi
exit 0


##############################################################################
# configure directory and file permissions
# application name system-discovery-service
##############################################################################
%files

%attr(0754,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service
%attr(0755,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service/install
%attr(0755,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service/install/dell-system-discovery-service
%attr(0755,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service/image
%attr(0755,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service/image/system-discovery-service
%attr(0755,system-discovery-service,dell) /opt/dell/cpsd/system-discovery-service/conf/
