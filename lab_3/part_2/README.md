### Part 2

Continuing onwards from part 1:

#### Updating Service Account permissions
- In the cloud console dashboard, go to "IAM" and select the principal labeled as "App Engine default service account".
- Click the pencil icon to edit it as before and assign the roles "Cloud SQL Instance User" and "Cloud SQL Admin".

#### Connecting App Engine to Cloud SQL
*There is a chance this is missing a step or two as there was some trial and error involved in getting this to work.*

- On the Cloud SQL Instances page of the cloud console, select your instance and then go to "Users". Then click "Add user account".
- Click the "Cloud IAM" radio button and in the "IAM Principal" field, enter the username of your App Engine service account (Everything before the @).
- Connect to the Cloud SQL instance and enter the following:
```
USE students;
GRANT ALL on studentRecords TO <user account name>;
```