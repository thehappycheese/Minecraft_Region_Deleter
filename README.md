# Minecraft Region Deleter

This python app asks you to select the region folder of your minecraft save and shows the .mca region files in a grid.
 
### The good news
 
 Since I only used standard python 3.4 libraries this should work on any opperating system.
 
### The bad news
 
I made this using TkInter for python and I had no idea what I was doing.

- there are no scroll bars
- or any other nice features

I think if i was to do this again I would use C# or something. At least then there would be a simple way to send the files to the trashcan.

### Requirements
- python 3.4
- [MCEdit] and/or Dinnerbone's coordinate  [calculator] so you can figure out which files to delete

### How to use
1.  On opening, the software should ask you to select the region folder of your minecraft save
2.  It will then show all the files in a grid pattern
3.  Check the checkboxes you want to delete
4.  ***Back them up first!***
5.  Chunks are not the same as regions. It's probably important you know that at this point because region files contain lots of chunks.
6.  Hit delete and hope for the best

Hope it helps someone :)

[MCEdit]:http://www.mcedit.net/
[calculator]:https://dinnerbone.com/minecraft/tools/coordinates/
