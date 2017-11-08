#!/bin/bash
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

echo "Installing Dell Inc. Seed PAQX components"

RETVAL=0

SERVICE_BASE=/opt/dell/cpsd/system-discovery-service

echo "Installing Dell Inc. Seed PAQX components"

if [ ! -d "$SERVICE_BASE" ]; then
    echo "Could not find directory - [$SERVICE_BASE] does not exist."
    exit 1
fi

usermod -aG docker system-discovery-service

/bin/sh /opt/dell/cpsd/system-discovery-service/image/system-discovery-service/install.sh -s

RABBITMQ_ENV=/etc/rabbitmq/cpsd-rabbitmq-env.conf

if [ ! -f "$RABBITMQ_ENV" ]; then

    touch "$RABBITMQ_ENV"

    /usr/bin/env echo "CREDENTIALS=/etc/rabbitmq/credentials.properties" >> "$RABBITMQ_ENV"
    /usr/bin/env echo "PASSPHRASES=/etc/rabbitmq/client/passphrases.properties" >>  "$RABBITMQ_ENV"
    /usr/bin/env echo "KEYSTOREPATH=/etc/rabbitmq/certs/client/keycert.p12" >> "$RABBITMQ_ENV"
    /usr/bin/env echo "TRUSTSTOREPATH=/etc/rabbitmq/certs/rabbitstore" >> "$RABBITMQ_ENV"

    chmod a+r "$RABBITMQ_ENV"
else
    echo "Found $RABBITMQ_ENV"
fi

export HOSTNAME=$(hostname -f)
export CREDENTIALS=/etc/rabbitmq/credentials.properties
export PASSPHRASES=/etc/rabbitmq/client/passphrases.properties
export KEYSTOREPATH=/etc/rabbitmq/certs/client/keycert.p12
export TRUSTSTOREPATH=/etc/rabbitmq/certs/rabbitstore


pushd /opt/dell/cpsd/system-discovery-service/install/dell-system-discovery-service/
docker-compose create
docker start dell-cpsd-system-discovery-service
popd

echo "Dell Inc. System Discovery Service components install has completed successfully."

exit 0
