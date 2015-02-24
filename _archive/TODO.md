To Do:

[X]    Add correct idomatic python coding style __main__

[?]    function-alize the script. Make a function for the output ("def
output", for instance), one that handles language, one that handles the command line
interface.
  - WIP: Going overboard with this isn't productive. Keeping it simple
    is better. Mostly this is is just adding more words to a simple
script without good reason. Allowing it to stay simple for now. May come
back to this if there is value. Will follow up with Nick/Brian

[x] Add file handling.
  [x] file_io is simple. Implement that first
  [x] Upgrade to the python CSV library if there is value to that. As it
turned out, the CSV lib made it a shit ton easier. I might go back and
implement the file_io way as a learning exercise.


[x] Multiple file outputs. With file handling decided and implemented, now we need multiple files. // going with single files for now.
Randomized localization, and let the user indicate which import to use.
  [x] Decide what files would be best to output and implement that.
  [x] Make a directory to keep them in // decided against this for now

[x] Boundary testing support? // yes, but in a separate utility
  [ ] White space characters
  [ ] Lots of data in each cell
  [ ] Special Characters in each cell
  [ ] Empty cells in each required category

[x] Localization support // yes. I decided on randomized languages for now, just to keep it simple. I can always make this more granular (allow the user to indicate a specific language in particular, for instance) if needed/desired.
