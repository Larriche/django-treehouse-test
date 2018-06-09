Below is a description of the challenge.I was expected to fill in the missing bits of this application to make it
pass all the tests.

Welcome to Django Karaoke!

We're going to put on a Karaoke party at our next Django conference and we need to prototype an app for it. I've included a basic bit of HTML and some tests but I'll need you to finish up the code in the `songs` app. Thanks for helping out!

Here are some details:

* Song model should:
  * have a title
  * have an artist (original performer)
  * have a performer (who's singing it for karaoke) (make this another model)
  * have a length (number of seconds in duration)
  * return '<title> by <artist>' when turned into a string

* Performer model should:
  * have a name
  * return the name when turned into a string

* Views:
  * list view, all of the songs
  * detail view, a particular song
    * tell who's performing it
  * performer view, a particular performer
    * list all of their songs

Feel free to add other features, too, if you want. Like maybe the minutes:seconds version of how long the song is?

You can check out the tests in songs/tests.py and run them with `python manage.py tests`.

Good luck!