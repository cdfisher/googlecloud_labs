### Part 1

Reading the text and marking the images with boxes around the text...for most of the images.

This largely follows [this guide](https://cloud.google.com/vision/docs/ocr) from Google.
##### Setting up
Using the locally-installed `gcloud cli`:
- Using either an existing project or a new one, `gcloud config set project <PROJECT_ID`, then enable the Vision API for the project with 
`gcloud services enable vision.googleapis.com`
- Grant the Storage Object Viewer role to your user account either in the IAM section of the cloud console dashboard or with `gcloud projects add-iam-policy-binding <PROJECT_ID> --member="user:<USER_ACCOUNT>" --role="roles/storage.objectViewer"`
- Install the client library with `pip install --upgrade google-cloud-vision`


##### Reading the text
Example code is included in `read_text.py`


##### Marking the text
- Install Pillow with `pip install pillow`

Example code is included in `mark_text.py`

Notice that Cloud Vision picks up the text in test and test3, but not in test2.
This image requires some preprocessing in order for the text to be recognized.