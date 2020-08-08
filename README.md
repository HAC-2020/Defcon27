# ARLO-Advanced-Robot-for-Logistics-Patrol-Operations

![Built with](https://img.shields.io/badge/BUILT%20WITH-RASPBERRY%20PI-critical?style=for-the-badge&logo=raspberry-pi)

ARLO is a robot that can be deployed in COVID-19 containment zones for delivery of essential supplies like sanitizers, masks improving safety in logistics and also surveillance of the area.


## PROBLEM IT SOLVES
The main problem we aim to solve is the safety concern in point to point delivery system in pandemics situation like we are facing right now. So, the main objective of our project is to develop a remote prototype that can be used to deliver small payloads of essential supplies in severe effected areas of COVID-19 called containment zones where in-person delivery is restricted. ARLO is capable of carrying and delivering small essential payloads like medical supplies with ease without the need of any contact of personnel (zero contact delivery). 

The idea is that, when there is a need to deliver essential supplies in a containment zone , ARLO can be deployed as a secondary transport for delivery. The primary transport like pickup truck can be used to reach near the delivery zone and from here, ARLO can be used to safely deliver essentials by the operating user to the drop point with the payoad attached to it. From this remote location the user can control ARLO with the help of live stream , streamed from the robot with the help of PiCamera which is mounted on top of it. ARLO can be maneuvered with the help of onscreen controls that control the robot and help the operating user to move the robot to the required location point. Also ARLO is equipped with onboard temperature sensors that relay this temperature data to user, incase of detection of high temprature , gives an alert to follow extreme precaution. This is 
kind of point to point deliver is safe, efficient (since it uses batteries ) and affordable (made with minimal hardware).

Also, the camera feed is used to monitor the containment area which is the patrol module of the robot. The system is equipped with some computer vision applications that are capable of detecting any violation in social distancing and raises an alert. This is possible with the help of feed from the Picamera to the web application which is then used by patrol module.
