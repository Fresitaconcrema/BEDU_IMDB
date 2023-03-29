Create Database project_imdb;

use project_imdb;

#drop table name_basics;
Create table name_basics (
ncosnt varchar(100),
primaryname varchar(600),
birthyear int,
deathyear int,
primaryprofession varchar(200),
knowfortitles varchar(350)
);

#drop table title_ratings;
Create table title_ratings (
tconst varchar(100),
averageRating decimal(8,4),
numVotes int
);

#drop table title_akas;
Create table title_akas (
titleid varchar(100),
ordering int,
title varchar(600),
region varchar(100),
language varchar(100),
types varchar(200),
attributes varchar(200),
isoriginaltitle varchar(100)
);

Create table title_crew (
tconst varchar (100),
directors varchar(100),
writers varchar(300)
);

Create table title_episode (
tconst varchar(100),
parenttconst varchar(100),
seasonNumber int,
episodeNumber int
);

#drop table title_principal;
Create table title_principal (
tconst varchar(100),
ordering int,
nconst varchar(100),
category varchar (300),
job varchar(300),
characters varchar(800)
);

truncate table title_basics;
#drop table title_basics;
Create table title_basics (
tconst varchar(100),
titletype varchar(100),
primarytitle varchar(4500),
originaltitle varchar(2500),
isadult int,
startyear int,
endyear int,
runtimeminutes int,
genres varchar(200)
);




Create table country (
region	VARCHAR(20),
country	VARCHAR(30),
alpha3code	VARCHAR(15),
alpha2code	VARCHAR(15),
pop	VARCHAR(15),
tests	VARCHAR(15),
testpop	VARCHAR(15),
density	VARCHAR(15),
medianage	VARCHAR(15),
urbanpop	VARCHAR(15),
quarantine	VARCHAR(15),
schools	VARCHAR(15),
publicplace	VARCHAR(15),
gatheringlimit	VARCHAR(15),
gathering	VARCHAR(15),
nonessential	VARCHAR(15),
hospibed	VARCHAR(15),
smokers	VARCHAR(15),
sex0	VARCHAR(15),
sex14	VARCHAR(15),
sex25	VARCHAR(15),
sex54	VARCHAR(15),
sex64	VARCHAR(15),
sex65plus	VARCHAR(15),
sexratio	VARCHAR(15),
lung	VARCHAR(15),
femalelung	VARCHAR(15),
malelung	VARCHAR(15),
gdp2019	VARCHAR(15),
healthexp	VARCHAR(15),
healthperpop	VARCHAR(15),
fertility	VARCHAR(15),
avgtemp	VARCHAR(15),
avghumidity	VARCHAR(15),
firstcase	VARCHAR(15),
totalcases	VARCHAR(15),
active30	VARCHAR(15),
active31	VARCHAR(15),
active1	VARCHAR(15),
active2	VARCHAR(15),
active3	VARCHAR(15),
newcases30	VARCHAR(15),
newcases31	VARCHAR(15),
newcases1	VARCHAR(15),
newcases2	VARCHAR(15),
newcases3	VARCHAR(15),
deaths	VARCHAR(15),
newdeaths30	VARCHAR(15),
newdeaths31	VARCHAR(15),
newdeaths1	VARCHAR(15),
newdeaths2	VARCHAR(15),
newdeaths3	VARCHAR(15),
recovered	VARCHAR(15),
critical30	VARCHAR(15),
critical31	VARCHAR(15),
critical1	VARCHAR(15),
critical2	VARCHAR(15),
critical3	VARCHAR(15),
casediv1m	VARCHAR(15),
deathdiv1m	VARCHAR(15)
);