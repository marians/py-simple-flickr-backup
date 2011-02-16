Simple Flickr Photo Backup in Python
====================================

I wrote this script in order to download all my original photos from my Flickr
account.

Requirements
------------

* Python (tested on 2.6.1)
* FlickrAPI module from http://stuvel.eu/flickrapi (thanks to Sybren A. Stüvel!)
* ElementTree module
* urllib module
* A Flickr API and the according secret. Get them at http://www.flickr.com/services/api/keys/
* a graphical system like Mac OS X, Windows or Linux. A simple text shell probably won't work
	due to OAuth authentication.
* Your Flickr user ID. Mine is '16126796@N00'

Usage
-----

* drop the script to the folder where you want to download all your photos to
* edit the script file in order to contain your api_key, api_secret and user_id
* run the script in the command line, e.g. with

	python get_my_photos.py

* When your browser opens, asking you to authorize an app for Flickr access, hit the Accet button.
* Turn back to the console and hit ENTER
* Now lean back and relax

Known Problems
--------------

* Photos are named by their ID. The original file name isn't stored on flickr.
* The file modification date/time is set to the current time when downloaded.
* Downloading is slow due to being single-threaded.

License
-------

None whatsoever. Do what you like.

