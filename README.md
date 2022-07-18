# I used this script to download pdf files from telegram group and upload them to google drive

### ```Prerequisite:```
> you will need to have a google account and a google drive account
    - you can use this link [google account](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp) to create a google account 
    - you can use this link [google drive account](https://drive.google.com/drive/my-drive) to create a google drive account 
   

> you will need to have a telegram account


> you will need to install the following packages:

- pip install google-api-python-client   
 
- pip install PyDrive  (if you want to upload to google drive) 

- pip install telethon  

    - you can get you api key and api hash from [here](https://my.telegram.org/apps)
> you will need to edit the file named `.env` under directory called Credentials  

  - replace the `api_id` and `api_hash` with your own values 

> you will need to replace a file named `client-secret.json` 
 
- You can retrive your client and secret key from [google drive api](https://console.cloud.google.com/apis/credentials)
  - First you need to create a project
      
  - select your created project from the notification tab. this will make the project active    

  - create OAuth consent screen
  
  - Then you need to create a credentials file by clicking on the project name and then click on  create credentials
          - click on the credentials tab
          - click on OAuth client ID
          - select Desktop application as your application type
          - click on the Create button
      
  -click on the credentials tab     

      - click on the application name you just created under OAuth section    
          
        ![creadential](./img/Screenshot380.png?raw=true "Title")     
        
  - Then you need to click on the "Download JSON" button

        ![download-json-file](./img/Screenshot380.png?raw=true "Title")

  
> you will need to edit the file named `settings.yaml` in the same directory as this script 

- replace the `client_id` and `client_secret` with your own values

- replace the `group_id` with your own value


- replace the `folder_id` with your own value
