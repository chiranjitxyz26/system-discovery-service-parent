/**
 * Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved. Dell EMC Confidential/Proprietary Information
 */

package com.dell.cpsd.system.discovery.service;

import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.support.SpringBootServletInitializer;

import com.dell.cpsd.system.discovery.service.message.config.PaqxPropertiesConfig;

/**
 * Startup application.
 * <p>
 * Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved. Dell EMC Confidential/Proprietary Information
 * </p>
 */
@SpringBootApplication
public class Application extends SpringBootServletInitializer
{

    /**
     * Main method that helps to start the application
     *  <p>
     * To execute the application in a local machine which does not have amqp setup for rabbitmq, 
     * update the rabbitmq.properties file mentioned in {@link PaqxPropertiesConfig}
     * </br>
     *  - Change remote.dell.amqp.rabbitHostname = {required_host}   - example: localhost
     * </br>
     *  - Change remote.dell.amqp.rabbitPort     = 5672
     * </br>
     *  - Add remote.dell.amqp.rabbitUsername= {user_name}
     * </br>
     *  - Add remote.dell.amqp.rabbitPassword= {password}
     * </br>
     *  - Change remote.dell.amqp.rabbitIsSslEnabled = false
     * </p> 
     * @param args
     *            {@link String[]}
     */
    public static void main(String[] args)
    {
        new Application().configure(new SpringApplicationBuilder(Application.class)).bannerMode(Banner.Mode.LOG).run(args);        
    }
}
