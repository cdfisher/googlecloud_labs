## Deploying to Google App Engine
This is a relatively minimal example of how to deploy a Python app using Flask to Google App Engine. All necessary files are included in this repo.

This mostly follows [this guide from Google](https://cloud.google.com/build/docs/deploying-builds/deploy-appengine?authuser=1&cloudshell=false)
but includes some steps that guide fails to cover.

### Steps
- Enable the App Engine API in the cloud console.
- Install the `gcloud cli` locally. [Link to installer](https://cloud.google.com/sdk/docs/install) 
- `cd` to the `/app/` directory.
- Run `gcloud auth login` and go through the in-browser prompts that pop up.
- `gcloud config set project <PROJECT_ID>`, where `PROJECT_ID` is the ID listed on the cloud console "Dashboard" page under "Project Info".

The quickstart guide from Google misses a few now-important steps, covered [here](https://www.googlecloudcommunity.com/gc/Serverless/Error-during-gcloud-app-deploy-for-GAE-app-quot-Failed-to-create/m-p/777154):
- Go to "Project Settings" -> "IAM" and find the principal with the name "App Engine default service account". Click the pencil icon "Edit principal".
- Search and add the following permissions: "Artifact Registry Create-on-Push Writer", "Storage Admin", and "Logs Writer".
- `gcloud app deploy`
- Select the region where the app should be hosted (15 is northamerica-northeast1 at the time of writing).
- When prompted to continue, enter `Y`
- After deployment is finished, do `gcloud app browse` to open the application in your browser.
