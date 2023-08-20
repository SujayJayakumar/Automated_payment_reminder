# MaintainanceFee_Remainder
An automatic sms reminder to remind residents to complete the payment towards layout maintainance after reading an excel sheet with payment status and resident details


This project (Main file is "code.py") uses an excel sheet to source the input , the fields of which are of the following order


House#	|| Sub Unit ||	Name	|| Latest Rcpt	|| Amt	|| From ||	To	|| Contact number	|| Paid Members
![image](https://github.com/SujayJayakumar/MaintainanceFee_Remainder/assets/113993766/9262b297-d0e4-4ef6-bf1c-ef0bdcad00f8)


The pandas module reads the excel file and iterates through each record and checks is the payement status is unpaid. In case its already paid,it moves to the nxt resident.
If unpaid, it records the phone number of the coressponding resident and uses the 3rd party module (currently, twilio module) to send a reminder msg to that contact and prints the number of the target contact.
(Fields without contact information are to be saved with "-" in place of contact number)


Another file name keys.py is used to save the authenication code and token of the registered twilio account which is then imported to the code.py (main file) to send the msgs

Also, refer to the "python libraries to b installed.txt" to install the necessary modules in python using pip command in the terminal.

twilio_msg.py is a dummy file with the syntax needed to send the msg as per twilio module.

