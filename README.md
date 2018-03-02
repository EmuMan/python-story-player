# python-story-player
A very quick thing I made in a day.  It is designed to read a JSON file, and if in the correct format, it will be able to run it like a story-based game.  There is a very quick and very WIP story already there (alps.json).

I know I didn't really need to include the packages folder as the only thing in it is "dprint.py" (stands for delayed print), but IMO it makes things cleaner because it feels nice to just have one python file in the root directory.

## Proper JSON format
If you want to make your own story, you have to follow these formatting rules or it will not work.  A really great tool for this is [JSON Editor Online](https://jsoneditoronline.org/), which has a really nice UI for easily adding blocks to a story and is also nice if you don't want to install anything.
Each dictionary, enclosed in curly brackets, have four elements.  Of course, special dictionaries, like endpoints and redirections do not follow this, but standard ones do.  These four things are:
* The displayed text ("text")
* The two choices (in list form) ("opts")
* Both of the choices as separate dictionaries
For example, this would be a *mostly* acceptable block:
```
{
  "text": "This is what will be displayed as the story progression.",
  "opts": ["option1", "option2"],
  "option1": {
    "this is another dictionary": "that follows the same conventions as the last one"
  },
  "option2": {
    "this is another dictionary": "that follows the same conventions as the last one"
  }
}
  ```
The only thing about this that would not work is the fact that trying to actually use any of the options will move you into an invalid list, as the subdictionaries are completely incorrect in terms of content.
  
As I mentioned before, there are some exceptions.  If you do not supply any options (don't define the "opts" list), the block will be regarded as an endpoint and after the text plays, *The end!* will show up on screen and you will be asked if you want to play again.

The other exception to this is a redirection.  This is used when you want to move to a specific part of the story to avoid copy-pasting long parts of the story if you want two different ways to end up at the same place.  To do this don't define any options, but instead, use the "goto" lists.  In the list, just enter the options that need to be entered in order to get to the spot you want to get to.  For example, this would work
```
{
  "text": "This is what will be displayed as the story progression.",
  "goto": ["yes", "forward", "left", "stop", "open", "run"]
}
```
provided that you have the proper dictionaries and subdictionaries.

As you can probably imagine, these stories can get quite messy, which is why I recommend [JSON Editor Online](https://jsoneditoronline.org/) for ease of comprehension and editing if you don't have anything else installed.  You can also use the tool to remove spaces to make the file extra hard for people to read without using the engine.

### Special chars
There are two special characters you can include in your JSON story: ~ and ^.  ~ can be placed anywhere to create a half-second pause (ideal after periods and such), and ^ can be used to create a new line (think pressing enter).  **DO NOT** USE \n!!! This will make the JSON file unreadable, and it will not be able to load into the game.  Use ^ instead.

## Running stories
To run your story, simply launch "play.py" and enter the name of the game file you want to run (must be moved into the 'games' folder).  You can learn more about how to run Python for your OS and such from other sources online, and as far as I can tell, this should work with Python 2.X as well, but it hasn't actually been tested.

The alps.json example in the code, while, again, it isn't complete and doesn't fully work, should have sufficient examples to learn from.  I will also be working on that story, so it will get better.
