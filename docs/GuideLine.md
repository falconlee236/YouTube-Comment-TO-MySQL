# Guideline

authorship: https://python.gotrained.com/youtube-api-extracting-comments/

### **Project Setup**

In order to access the YouTube Data API, you need to have a project on Google Console. This is because you need to obtain authorization credentials to make API calls in your application.

Head over to the [Google Console](https://console.developers.google.com/projectselector2/apis/dashboard) and create a new project. One thing to note is that you will need a **Google account** to access the console.

Click **Select a project** then **New Project** where you will get to enter the name of the project.

[![Create New Google Project](https://i0.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot3.png?resize=525%2C252&ssl=1)](https://python.gotrained.com/?attachment_id=1408)

 

Enter the project name and click **Create**. It will take a couple of seconds for the project to be created.

[![Google New Project](https://i0.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot2-e1551474013610.png?resize=525%2C414&ssl=1)](https://python.gotrained.com/?attachment_id=1407)

 

### **API Activation**

Now that you have created the project, you need to enable the YouTube Data API.

Click **Enable APIs and Services** in order to enable the necessary API.

[![img](https://i2.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot4.png?resize=525%2C252&ssl=1)](https://python.gotrained.com/?attachment_id=1410)

 

Type the word “youtube” in the search box, then click the card with **YouTube Data API v3** text.

[![img](https://i2.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot5.png?resize=525%2C252&ssl=1)](https://python.gotrained.com/?attachment_id=1411)

 

Finally, click **Enable**.

[![img](https://i0.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot6.png?resize=525%2C236&ssl=1)](https://python.gotrained.com/?attachment_id=1412)

 

### **Credentials Setup**

Now that you have enabled the YouTube Data API, you need to setup the necessary credentials.

Click **Create Credentials**.

[![img](https://i2.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot7.png?resize=525%2C249&ssl=1)](https://python.gotrained.com/?attachment_id=1415)

In the next page click **Cancel**.

[![img](https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot8.png?resize=525%2C251&ssl=1)](https://python.gotrained.com/?attachment_id=1416)

 

Click the **OAuth consent screen** tab and fill in the application and email address. .

[![img](https://i2.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot10.png?resize=525%2C250&ssl=1)](https://python.gotrained.com/?attachment_id=1417)

 

Scroll down and click **Save**.

[![img](https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot11-e1551475169867.png?resize=503%2C326&ssl=1)](https://python.gotrained.com/?attachment_id=1418)

 

Select the **Credentials** tab, click **Create Credentials** and select **OAuth client ID**.

[![img](https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot12.png?resize=525%2C250&ssl=1)](https://python.gotrained.com/?attachment_id=1419)

 

 

Select the application type **Other**, enter the name “YouTube Comment Extractor”, and click the **Create** button.

Click **OK** to dismiss the resulting dialog.

[![img](https://i0.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot13-e1551474156606.png?resize=525%2C312&ssl=1)](https://python.gotrained.com/?attachment_id=1420)

**Click the file download button** (Download JSON) to the right of the client ID.

[![img](https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/02/screenshot14.png?resize=525%2C250&ssl=1)](https://python.gotrained.com/?attachment_id=1421)

Finally, move the downloaded file to your working directory and rename it `client_secret.json`.