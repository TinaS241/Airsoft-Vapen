# Airsoft Vapen
Project OverView:

What are the major features of your web application? 
To allow the user to input their own custom airsoft build into the website. 

Problem to solve? 
To show off custom airsoft guilds and place to allow the user to see builds people have done and where to buy the parts, get first-hand user info from players. 


What libraries or frameworks will be used? None right now, FrameWork will be Django Framework


As a user, I want to be able to add a picture of my airsoft gun and what part i have install and give info about what i have done to it.  I want to be able to find other users’ builds and put them on a favorites list and rate them and post a comment to ask about the build. I want a link to where they bought the parts and gun.


Data Model
- User: 
    - user profiles
- Custom gun models:
    - title, author, body, created, updated, url, picture. 
- Comment model:
     - author, body, created


# Task

#### Must Half:
- Store airsoft gun info, edit and delete:
    - Custom gun model for store info. 

- Filter by airsoft guns type and ranks EX: M4, Aks, pistols
    - Function methods to filter by type 
- Display all airsoft guns within there area. 
    - html component from vue
- Comment select and allow a user to add edit and delete comments. 
    - Comment model to show and update what was posted. 

 #### Maybes: 
- Rate systems (Bootstrap check in to that or vuetify)
    - Bootstrap rate system attached to each gun to update
- Url links to videos from youtube base on guns
    - embed youtube videos for each gun on page. 


# Schedule
#### WEEK 1:  
- 1-3 days: Setting up Django rest framework and API and Users.
- 2 days: Store user input info and display it to the webpage with URL link to where to buy same parts  

#### WEEK 2:

- 1 day: Build comment area for each input gun and display pictures
- 2 day: display all airsoft gun by type of airsoft guns added 
- 3-4 day: Add filter by gun types for the user to pick to view


#### WEEK 3:
- 1 days: working on the filter part of the website
 - 2-3 days: CSS Make the website and layout using able on mobile on PC
