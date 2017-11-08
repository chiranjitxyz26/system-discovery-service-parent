/**
 * Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved. Dell EMC Confidential/Proprietary Information
 */

package com.dell.cpsd.system.discovery.service.message.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.PropertySources;

import com.dell.cpsd.si.config.PropertiesConfig;

/**
 * The configuration for the client.
 * <p>
 * Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved. Dell EMC Confidential/Proprietary Information
 * </p>
 */
@Configuration
@PropertySources({@PropertySource(value = "classpath:META-INF/spring/system-definition/rabbitmq.properties", ignoreResourceNotFound = true),
    @PropertySource(value = "file:${CREDENTIALS}", ignoreResourceNotFound = true),
    @PropertySource(value = "file:${PASSPHRASES}", ignoreResourceNotFound = true)})
@Primary
public class PaqxPropertiesConfig extends PropertiesConfig
{

}
