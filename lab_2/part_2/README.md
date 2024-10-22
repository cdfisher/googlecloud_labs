### Part 2
#### Deploying multiple app versions
- `cd` to the `part_2/app/` directory.
- Configure `main.py` the same way as in part 1 of this lab, or just reuse your app from that and modify main.py manually to specify versions rather than commenting and uncommenting lines.
- `gcloud app deploy version=v1`
- After that deploys, edit `main.py` to comment out the two lines mentioning version 1 and uncomment the two lines mentioning version 2.
- `gcloud app deploy version=v2`
- Then do the same steps as above for version 3
- After deploying all three versions, go to "Versions" under the "App Engine" section of the cloud console dashboard and click "Split traffic"
- Under "Split traffic by", select "Random" (Otherwise you'll have a hard time hitting the different versions on the same machine in a short timeframe)
- Under "Traffic allocation", set your splits across versions as desired and then click "Save"
- Navigate to the "Services" section of the App Engine dashobard and click the name of your service to open a new tab. This will select a version of the service to use at random.
***Simply refreshing the page will cause it to use the same (cached) version. You have to open new tabs from the Services list to hit different versions of the app.***
