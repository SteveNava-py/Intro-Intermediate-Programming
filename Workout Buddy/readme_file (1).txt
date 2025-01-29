Project Title: 
Brief description of the project idea: The main idea of this project was to create a smart user interface that helps the user achieve their weight loss goals. The user should create a profile where they upload user data. Once user data has been uploaded, various functions calculate different metrics for the user to help streamline their goals such as their BMR, heart rate data, and burned calories. With the ability to track calories burned using the HR monitor along with estimating the number of calories the user should eat, the user can then continue using the program to reach their goals. 

Team Member Names:Brayden Gilley, Steven Navarrette, Zach Ryan


/**********************************************************************
 *  Log all help, collaboration, and outside resources you've used for this project. List all external Python library names you used. Add links to the websites you have used as resources.
 **********************************************************************/
https://youtu.be/YXPyB4XeYLA?si=kVLzPNUkZJXoX0Ju

https://github.com/WorldFamousElectronics/Raspberry_Pi/blob/master/PulseSensor_Arduino_Pi/PulseSensor_Arduino_Pi.md

https://docs.python.org/3/library/dialog.html


/**********************************************************************
 *  List step by step insturctions on how to use your project. If someone would take your code and your circuit and hardware, how would they start using the application. This should server as a user manual. 
 **********************************************************************/
The workout buddy application consists of the python code, arduino code, Hr monitor, and arduino. To set up the physical aspect of it, one needs to plug the HR monitor into the arduino. The arduino code needs to to be actively running before starting to run the python code. Once the user runs the python code, they will go through the create a profile/ log in process. They then enter their metrics and weight gaols. After this, the user can select start workout, where they will choose from a selection of workouts and then one more button to start their workout. At this time, the user should use the HR monitor wearable to keep the HR monitor attached to their body. The HR monitor will keep track of their heart rate and display the calories burned once the user finished their workout. 


/**********************************************************************
 *  Describe any serious problems you encountered while working on this project and how you solved/came around the problems.                  
 **********************************************************************/
Many of the problems we experienced came up integrating the HR monitor with coding / GUI. The heart rate monitor was no doubt a cheap one and very frequently gave us faulty reads where the supposed heart rate would shoot up well above 200. So, we decided to implement a filter into our code that would only accept HR values between 40 and 120. Also, their would be values that greatly changed from previous values even though the return rate as one HR every 1 second. So, if the new HR value is greater than 10 beats away from the previous, we would ignore that value until the new value normalized to within 10 beats. We wanted to have the HR monitor be wireless but we realized we were short on hardware, and to solve the problem of having massive wires going everywhere, we created almost like a wearable device that would encapsulate the HR monitor and the arduino. Another problem we faced is that we couldn't get the arduino code into python because we were using the wrong port on the arduino, to which we ended up finding the right port and transfered the arduino code. 


/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing this project and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/
 One thing we learned is that combining hardware and software seamlessly is much more difficult than we anticipated. One thing we wanted to do (and spent hours and hours trying) but were not able, is to actively update the amount of calories the user had burned onto the workout screen so they could see it while they are working out. We were able to get the number of calories burned from the start of the workout to a specific point in time, but then continuing to update it while not losing the data was somehow fooling us. It could have been from the fact that the last 2 days have been us working at many hours through the night as well as Steven having all the hardware. We were constanlty having to come up with changes or ideas to the code, emailing it to steven, having him run it and faceTime us so we could see where the errors were. That part was definetly a struggle and I really wish we had started working on that sooner so we could have gotten outside help, as I think that would have been a major benefit to our program. Instead, we were only able to calculate the total calories burned and average heart rate once after the user finished their workout in a post workout review screen. ( I didnt mention this in the one above since we didnt find a way to fix it). 

