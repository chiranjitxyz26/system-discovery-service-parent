#!/bin/bash
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

echo "Removing Dell Inc. System Discovery Service components"

/bin/sh /opt/dell/cpsd/system-discovery-service/image/system-discovery-service/remove.sh

echo "Dell Inc. System Discovery Service components removal has completed successfully."

exit 0
