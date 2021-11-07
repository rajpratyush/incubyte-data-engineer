# Incubyte Assessment

I own a Multi-Specialty Hospital chain with locations all across the world. My hospital is famous for Vaccination. Patients who come to my hospital (across the globe) will be given a User Card with which they can access any of my hospital in the world.

We maintain all customers in one database. There are heaps of customers with user cards to my hospital. So, I decided to split up the customers based on the country and load them into corresponding country tables. To pull the customers as per Country, my developers should know what are all the places the Customer Data is available. So, the data extracting will be done by our Source System. They will pull the all the relevant customer data and will give us a Data file.

## The Problem

Developers will pull the all the relevant customer data and will give us a Data file.

In design documents, you will have:

File Name Specification – Name String, Extension of the files

Date and Time format of the File – YYYYMMDD, HHMMSSTT or any other format

Header Records Layout – |H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active

Details Record Layout – |D|John|123456|20101012|20121013|MVD|Paul|NSW|AU|06031987|A

Detail Records-
| File Position | Column_Name         | Field Length | Data Type | Mandatory | Key Column |
|---------------|---------------------|--------------|-----------|-----------|------------|
| 1             | Customer Name       | 255          | VARCHAR   | Y         | Y          |
| 2             | Customer ID         | 18           | VARCHAR   | Y         | N          |
| 3             | Customer Open Date  | 8            | DATE      | Y         | N          |
| 4             | Last Consulted Date | 8            | DATE      | N         | N          |
| 5             | Vaccination Type    | 5            | CHAR      | N         | N          |
| 6             | Doctor Consulted    | 255          | CHAR      | N         | N          |
| 7             | State               | 5            | CHAR      | N         | N          |
| 8             | Country             | 5            | CHAR      | N         | N          |
| 9             | Post Code           | 5            | INTEGER   | N         | N          |
| 10            | Date of Birth       | 8            | DATE      | N         | N          |
| 11            | Active Customer     | 1            | CHAR      | N         | N          |


The sample file format will be:

|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active

|D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A

|D|John|123458|20101012|20121013|MVD|Paul|TN|IND|06031987|A

|D|Mathew|123459|20101012|20121013|MVD|Paul|WAS|PHIL|06031987|A

|D|Matt|12345|20101012|20121013|MVD|Paul|BOS|NYC|06031987|A

|D|Jacob|1256|20101012|20121013|MVD|Paul|VIC|AU|06031987|A



### Note: In sample file given above post code not mentioned but it is present in Detail Records. I have written script according to sample file i.e. post code is not considered in code/script.




## Output
* Script or program to read data from file and load into tables. All customers related to India will go to Table_India and so on.

Script and data file for this is in Data and code folder.




### Intermediate tables will look like below:

![Tree](https://github.com/amoljkatkar/incubyte_assessment/blob/main/screenshots/screenshot1.png)



### Tables created in incubye database:

![Tree](https://github.com/amoljkatkar/incubyte_assessment/blob/main/screenshots/screenshot3.png)


### Queries on tables:
![Tree](https://github.com/amoljkatkar/incubyte_assessment/blob/main/screenshots/screenshot2.png)
