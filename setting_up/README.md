# Setting up a GCP project for App Engine and Cloud SQL
This covers the steps for setting up a project to use both App Engine and CloudSQL. The steps here are largely duplicated from other labs and it's possible something isn't necessary, but this process got a test project working at the time of writing.

## Steps
- Make sure to have the `gcloud cli` installed locally. [Link to installer](https://cloud.google.com/sdk/docs/install) 
- Enable the App Engine Admin API and Cloud SQL API in the cloud console.
- In your terminal (cmd/bash/zsh etc) run `gcloud auth login` and go through the in-browser prompts that pop up.
- `gcloud config set project <PROJECT_ID>`, where `PROJECT_ID` is the ID listed on the cloud console "Dashboard" page under "Project Info".
- Go to "Project Settings" -> "IAM" and find the principal with the name "App Engine default service account". **You may have to attempt to use `gcloud app deploy` before this service account appears in the list.** Click the pencil icon "Edit principal". 
- Search and add the following permissions: "Artifact Registry Create-on-Push Writer", "Storage Admin", and "Logs Writer".

### Deploying an app to App Engine
- `cd` to the directory which has your app and `app.yaml`.
- `gcloud app deploy`
- Select the region where the app should be hosted (15 is northamerica-northeast1 at the time of writing).
- When prompted to continue, enter `Y`
- After deployment is finished, do `gcloud app browse` to open the application in your browser.

### Cloud SQL setup

This portion seemed easier using Cloud Shell and following [this guide](https://cloud.google.com/sql/docs/mysql/connect-instance-cloud-shell).
##### Creating the instance
- In the cloud console, go to the Cloud SQL Instances page and click "Create instance".
- Click "Choose MySQL", and enter a name for the instance in the "Instance ID" field. Then in the "Password" field, enter a password for the `root` user. Then click "Create instance"

##### Connecting to the instance
- In the cloud console, open Cloud Shell. It may be necessary to run `gcloud auth login` and/or `gcloud config set project [PROJECT_ID]`
- `gcloud sql connect <instanceName> --user=root`. Then click "Authorize" in the dialogue, and enter the root password.
- From here, the `mysql` prompt should appear

##### Creating the database and uploading data
To use the example from class:
- `CREATE DATABASE students;`, then: `USE students; CREATE TABLE studentRecords (studentID VARCHAR(255), studentName VARCHAR(255));`
- To show the data in the table at any point, do `SELECT * FROM students`

## TODO 
Uploading data from a CSV to Cloud SQL


### Cleaning up

#### App Engine:
- Go to App Engine -> Settings -> Application Settings -> Disable Application

#### Cloud SQL:
- Go to Cloud SQL Instances -> select your instance to open "Instance details" -> Click "Delete" in the icon bar at the top of the page.