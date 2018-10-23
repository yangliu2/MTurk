# Mturk

**This package will be used to give task to Amazon's Mechanical Turks to label picture manually. It can probably be used to do other tasks on Mturk as well.**

I learned all this through the MTurk tutorials. https://blog.mturk.com/tutorials/home.

#### Prep work
Have the following accounts:
1. AWS
2. Mechanical turk prod
3. Mechanical turk sandbox

Link both sandbox and prod accounts to AWS, useing **root** account.

#### Set up aws keys
In `~/.aws/credentials`, include aws_key and aws_secret in this format.
```
[AWS]
aws_access_key_id = <access key>
aws_secret_access_key = <secret>
```
'AWS' is the profile name used to login AWS using Boto3 clinet API.

#### Create hits
Run `CreateHits.py` to create his. It basically load the `template.xml` on a website. First use `get_balance()` function to get the current balance. Switch between prod and sandbox accounts to find appropriate balance on each. 

Change image names by loading image links from website (S3), and inserted into the template via `modify_page()`. It will loop through all the images names and create separate 'hits'. Each hits return a unique hit ID, all hits link to the same place on Mturk. The images are severed in reverse order, first in last out. 

After each run, it will keep record of the last request in `last_hits.csv` and log all request in `log.csv`.

#### Check results
Once all hits are done, use `GetResults.py` to find all results. It will load all hits using the hit IDs and return back a json dictionary. 
