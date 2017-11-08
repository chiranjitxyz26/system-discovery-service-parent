#!/bin/sh
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#
CONTAINERID=$(basename "$(cat /proc/1/cpuset)" | cut -c 1-12)
java -Xms64m -Xmx192m -Dspring.profiles.active=production -Dcontainer.id=$CONTAINERID -jar /opt/dell/cpsd/system-discovery-service/lib/system-discovery-service*.jar -Dlog4j.configuration=file:/opt/dell/cpsd/system-discovery-service/conf/system-discovery-service-log4j.xml