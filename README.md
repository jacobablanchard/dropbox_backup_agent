# dropbox_backup_agent

This is a small project I used to practice using API's and learning about containers!

## So, what does it do?

This program will copy whatever is in the DROPBOX_LOCATION filepath on Dropbox to the LOCAL_LOCATION filepath.
For my use case, I was copying my Keepass database in Dropbox to my local NAS

## Ok, so that's kinda cool - How do I run it?

* Clone the repo (obviously)
* Update the docker-compose.yml file
  * volumes
    * Replace "{Place on local machine for storage}" with the directory you want the file to be downloaded to
  * environment
    * DROPBOX_TOKEN: Your dropbox api token
    * DROPBOX_LOCATION: Filepath to the file you want to back up
    * LOCAL_LOCATION: Where the file should be downloaded to
* If you don't live in the central timezone, you'll also probably want to update the [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) in the Dockerfile to the appropriate value of 'TZ database name'
* Run it! `docker-compose up -d`
