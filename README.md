# Service-Reminder

***Service Reminder*** is a project can be used Create a series of Calendar Event for any service automatically. The Application is written in Python (2.7) and Currently supports only Gmail account to send the Calendar events.

# How to Use

**Step 1 : Install the Application**

Application can be installed by cloning this repository to your directory. After cloning the repo, go to the project directory and run  ***`pip install --upgrade .`***

After the installation you can check the application status by running ***`reminder --help`***

**Step 2 : Creating a Configuration file**

 A configuration file is needed for the application, the structure of the file should be **/etc/reminder/reminder.conf**.
 An email [supports only Gmail as of now] address and Password should be entered in the created file under the DEFAULT section, which is needed to send the calendar invite.

 Sample conf file is available in [here](reminder.conf.sample).


**Step 3 : Adding the Services**

You need to add a service first before sending the reminder.

Command to create a sample service is,

***` reminder add --name Bike --date 01/07/2015 --interval 15,30,45 --enddate 01/07/2017 --time 1900 --before 1w `***

After running this command a section will get created in the conf file you have created before, which will be used to create the calenadr invite.

You can also delete this section by running,

***` reminder delete --name Bike `***


**Step 4 : Listing the Services**

After adding some services to the file, we can list all the services created using the below command,

***` reminder list `***


**Step 5 : Creating the Reminder**

This function is not developed yet, Idea here is to take all the services defined in the conf file and send a reminder to the given email address using the gmail account defined in conf file.
