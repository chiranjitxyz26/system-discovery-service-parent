#!/bin/bash
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

RETVAL=0
SERVICE_BASE=/opt/dell/cpsd/system-discovery-service

echo "Removing Dell Inc. System Discovery Service docker image."
docker stop system-discovery-service

docker rmi IMAGE_NAME_STANDIN:IMAGE_TAG_STANDIN
rm -rf ${SERVICE_BASE}/logs

echo "Dell Inc. System Discovery Service docker image removed successfully."

exit $RETVAL