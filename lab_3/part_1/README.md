### Part 1

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
