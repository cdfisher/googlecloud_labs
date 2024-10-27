# Setting up a GCP project for App Engine and Cloud SQL
This covers the steps for setting up a project to use both App Engine and CloudSQL. The steps here are largely duplicated from other labs and it's possible something isn't necessary, but this process got a test project working at the time of writing.

## Steps
- Make sure to have the `gcloud cli` installed locally. [Link to installer](https://cloud.google.com/sdk/docs/install) 
- Enable the App Engine Admin API, Cloud SQL API, and Cloud SQL Admin API in the cloud console.
- In your terminal (cmd/bash/zsh etc) run `gcloud auth login` and go through the in-browser prompts that pop up.
- Do this same process again with the command `gcloud auth application-default login`
- `gcloud config set project <PROJECT_ID>`, where `PROJECT_ID` is the ID listed on the cloud console "Dashboard" page under "Project Info".
- Go to "Project Settings" -> "IAM" and find the principal with the name "App Engine default service account". **You may have to attempt to use `gcloud app deploy` before this service account appears in the list.** Click the pencil icon "Edit principal". 
- Search and add the following permissions: "Artifact Registry Create-on-Push Writer", "Storage Admin", "Logs Writer", "Cloud SQL Instance User", and "Cloud SQL Admin".

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
- Click "Choose MySQL", and enter a name for the instance in the "Instance ID" field. Then in the "Password" field, enter a password for the `root` user. Open the "Flags" section, click "Add flag" and add `cloudsql_iam_authentication` with the value set to on.
- Optionally, set region to `northamerica-northeast1`, although this isn't super necessary for just a demo. **For demo purposes, set "Zonal availability" to "single zone". This reduces the cost but shouldn't be used in production environments.**
- Click "Create instance". It may take a few minutes for the instance to spin up. When I did it, starting the instance took a bit over 5 minutes.

##### Connecting to the instance
- In the cloud console SQL dashboard, on the "Overview" page, note the contents of the "Connection name" box under "Connect to this instance"
- In the cloud console, open Cloud Shell. It may be necessary to run `gcloud auth login` and/or `gcloud config set project [PROJECT_ID]`. If you open cloud shell using the "Open cloud shell" link in the "Connecting to this instance" box, this should already be set and the command to connect should be pretyped for you.
- If the command to connect isn't prefilled, do `gcloud sql connect <instanceName> --user=root`. Then click "Authorize" in the dialogue, and enter the root password.
- From here, the `mysql` prompt should appear

##### Creating the database and uploading data
To use the example from class:
- `CREATE DATABASE students;`, then: 

```
USE students;
CREATE TABLE studentRecords (studentID VARCHAR(255), studentName VARCHAR(255));
```

- To insert a record, do something like `INSERT INTO studentRecords (studentID, studentName) VALUES ("54321", "Chris");`
- To show the data in the table at any point, do `SELECT * FROM studentRecords;`

##### Uploading data from a CSV to Cloud SQL
- Go to the "Buckets" page in the cloud console and click "Create".
- Enter a name for the bucket, then click "Continue". The rest of the settings here are fine as defaults so click "Continue" several times until prompted to create the bucket, and do that.
- Open the bucket details for your bucket, click "Upload", and select your CSV file.
- On the Cloud SQL Instances page of the cloud console, select your instance and click "Import".
- Under "bucket-name/file-name", navigate to the file in your bucket and set "File format" to CSV.
- Under "Destination", select your database and input the name of your table. Then click "Import".

##### Connecting App Engine to Cloud SQL
*There is a chance this is missing a step or two as there was some trial and error involved in getting this to work.*

- On the Cloud SQL Instances page of the cloud console, select your instance and then go to "Users". Then click "Add user account".
- Click the "Cloud IAM" radio button and in the "IAM Principal" field, enter the username of your App Engine service account (Everything before the @).
- Connect to the Cloud SQL instance and enter the following:
```
USE students;
GRANT ALL on studentRecords TO <user account name>;
```


### Cleaning up

#### App Engine:
- Go to App Engine -> Settings -> Application Settings -> Disable Application

#### Cloud SQL:
- Go to Cloud SQL Instances -> select your instance to open "Instance details" -> Click "Delete" in the icon bar at the top of the page.