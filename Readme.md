
Weblink : https://6332-assign1.azurewebsites.net/


CSE 6332 Cloud Computing
Summer 2023, © DL, UTA, 2023
Programming Assignment 2
Introduction to Relational DB, SQL (Cloud)
Task:
You will get world earthquake data, import into SQL and with a web interface
allow users to find out (query) interesting information about those earthquakes.
Description:
Your assignment is to provide a local interface (using a web page, displayed in a
browser) to a cloud service that you will implement that will allow a user to upload
earthquake data and investigate it. (Creating the table doesn’t need to utilize
a web interface)
There are some “theories”:
There are more quakes in the early morning
There are more quakes in certain geographic locations (ring of fire)
Fewer quakes on weekends
And many, many others
Please go to:
https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
and get all earth quakes for the last 30 days (bottom right), which is a a .csv file,
place these on your cloud service provider and import this into SQL.
You may need to adjust negative lat and long. Why? How?
If you need local time, you can convert Z time (GMT) knowing 360 degrees is 24 hours.
This is close (DST, local diffs, etc. don’t make much of a difference)
There may be “bad” (anomalous, missing) data, need to add or modify (clean) data
This page also has a “schema” for the data.
Your cloud-based “service” will allow a user to:
+ Search for and count all earthquakes that occurred with a magnitude greater
than 5.0
+ Search for 2.0 to 2.5, 2.5 to 3.0, etc magnitude quakes for a one week,
a range of days or the whole 30 days.
+ Find earthquakes that were near (20 km, 50 km?) of a specified location.
+ Find clusters of earthquakes
+ Do large (>4.0 mag) occur more often at night?
And similar…
In later work you will try to “learn” from the data and show graphs and pictures.
Not yet (unless you want to).
You will use some type of RDB SQL to store and retrieve earthquake information.
And (of course) a friendly web UI.
You should handle conditions such as: missing data (fields, attributes), and similar.
Please, submit only on Canvas. Work must be individualized, but may be discussed in a
group.
You must submit this lab, working (or partially) by the due date.
Your program should be well commented and documented, make sure the first
few lines of your program contain your name, this course number, and the
lab name and number.
Your comments should reflect your design and issues in your implementation.
Your design and implementation should address error conditions.
