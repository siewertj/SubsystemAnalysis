# Subsystem Analysis
___

***currently in an experimental state.***

## Overview
This is intended to be a system for analyzing sub-systems, with first robot design in mind.The idea is to be able to create sub-systems by adding parts that are needed to create the sub-system. Analysis can be done to determine sub-system weight, cost, etc. Also want to be able to tie into an inventory management system so purchase decisions can be made.

### Goals
 - [ ] model atomic parts
 - [ ] building sub-assemblies
 - [ ] Inventory management
 - [ ] sub-assembly creation UI
 - [ ] atomic part creation UI
 
 ## Language Choice
 I have a few choices for the final language to actually write this in, each with different goals in mind.
 
 ### LabView
 First Robotics team 836, the RoboBees (the customer essentially) uses LabView for their robot development and thus creating this using LabView with perhaps some .dll plugins would make sense from a consistancy point of view. It also makes the UI element somewhat trivial though I'm not convinced this is the correct route. For one this would require a LabView installation to run and I don't think LabView is quite the right fit from a language perspective. Not to mention my skill in that area is somewhat lacking.
 
 ### Java
 RoboBees has a 'Special Projects' subteam that has developed a scouting app using Java so this is also a logical choice. This would make cross platform usage trivial and could easily be extended to include a phone app. The only runtime requirement here becomes the JVE which is included on most systems by default anyway. I suspect the performance difference to be minimal to non-existant since the loading and saving of configurations will probably take most of the cycle time. I imagine Java includes most of the libraries I would need as well. My biggest reservation here is that my Java knowledge is somewhat lacking though this could be a good opportunity to remedy that.
 
 ### Python
 I will likely be using python as the language for my rough-sketch run at this anyway; to get the high level architecture down. I find it easier to implement something and see how it works instead of making concrete descisions based on my pencil/paper analysis and python gives me a quick and easy way to do that. I know python far better than both LabView and Java so it will likely make development quicker. Python will also make it fairly easy to implement a webserver in the event that I wanted to run the configuration calculations remotely. As a good portion of the students (especially those on the programming sub-teams) are set on learning programming in college, I think python would be a good language to get them exposed to earlier rather than later. Of course the requirement here is that the system is running python which is trivial on Linux systems but can be a bit more involved on windows (though the recent installs seem to ease that process).
 
 ### C++
 From a personal perspective this seems like a good project candidate to start using the new C++11 standard (I've been supporting legacy projects/systems so I haven't been able to do a full C++11 project from the get-go which I would like to jump into). As stated above with the python, for students getting into programming C++ is a good language to expose them to simply because so many applications are designed in it. Of course this comes with a host of negatives (from a learning perspective) as the cross-platform game can be tricky at best, compilation (linking in particular) can be confusing to those not use to it (most ide's mitigate this of course), and this solution will most likely require the most 3rd party library support. Then of course there is the entire idea of pointers which I know from experience is not the easiest thing for new programmers to understand (probably a saving grace for me was that I learned to program in C but I watched a lot of guys who started from Java struggle when it came to our lecture on pointers in C++).
 
 ## User Interface
 This is something that I'm not sure how I want to do (part of it will rely on my choice of final language of course). I think I'll probably start with a sort of CLI interface (I'm a cli guy at heart but I recognize that it's not for everyone) and then build a GUI interface overtop of that. That being said my development will probably focus on the backend and not the user interface. Ideally I want to be able to give the UI as a project to a few of the students to develop.