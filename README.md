# Udacity-Azure-DevOps

# Overview

This project is done to fullfill Udacity A Cloud DevOps Using Microsoft Azure Nano Degree program.

In this Project, disposabale test environments and variety of automated tests were done using industry leading tools. In addition, moitoring tools are also used inorder to provide insight into an application's behaviour, and detrmine the root causes using Azure log Analytics.

# Project Tools and Environment 

In this project, the following tools were used 

* Azure DevOps
* Postman
* Terraform 
* JMeter 
* Selenium 

# Screenshots

* Azure Pipeline

![AzureDevOps Pipeline](screenshots/AzurePipeline.png)

## Stages of pipeline

* Terraform 

![Tfm](screenshots/terraformapply.png)

* Postman test results

![newman](screenshots/Postman_Regtest.png)

![newmansuc](screenshots/Postman_Validtest.png)

![newmangraph](screenshots/PostmanValidgraph.png)

![newmangraph](screenshots/PostmanRegressiongraph.png)

* Jmeter test results 

Endurance Test

![JmeterEnd](screenshots/JmeterEndurancepipeline.png)

Stress Test

![JmeterStr](screenshots/JmeterStresspipeline.png)

* Selenium test results

![Selenium](screenshots/SeleniumTest.png)

Custom Logs 

![Customlog](screenshots/CustomlogOutput.png)

* Azure alert setup 

Cpu usage alert

![cpual](screenshots/VMResAlertgraph.png)

* Azure alert Email notification setup 

![alertEmail](screenshots/EmailAlert.png)