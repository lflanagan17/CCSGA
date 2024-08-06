# STUDENT GOVERNMENT ELECTION VERIFICATION CODE

## Purpose: 
This code was created to help verify Colorado College Student Government Association's election results and report back an errors. This code uses the data obtained and formatted from qualtrics data but can be adapted to be used for other data sources 

## Using the code: 
### Inputs: 
 For the program to run affectively, a few steps needs to be taken. 
 1. Download election data as a CSV and place in "data" folder 
 2. enter election specific information as described in the comments and below in the input.py file 
#### Election descriptions: 
This program is for the use of either simple votes and ranked choice(singular seat and multiple seat).
For specifying election information for inputs, below are the options: 
'SIMPLE VOTE': Is a vote where there is only one option. Most often, this will be seen in an election that has one open seat and only two people running In spreadsheet holding election data, each row that reprsents a ballot should contain the name of the canidate they vote for in the cell that corrsponds to the column for the election question
| First name | Last Name  | Email  | OTHER ELECTION DATA | Vote on "position name" |
| ----------- | ----------- | ----------- | -----------| ----------- |
| Joe | Smith | jsmith@someemail.com| ... | Jane Doe |
| Jack | D | jackd@someemail.com| ... | Jane Doe |
| Betty | Timb | bettytimb@someemail.com| ... | John Doe |
'RANKED CHOICE' : a vote where ballots are casted by ranking the canidates. Two other options can occur: One where there is only one seat open and one where there are multiple seats open.In the spreadsheet that holds election data, each row that represents a ballot should contain a number underneath. Make sure the canidates name is following a "-"
| First name | Last Name  | Email  | OTHER ELECTION DATA | Rank for canidate -Jane Doe | Rank for canidate -John Doe |  Rank for canidate -Betty White | 
| ----------- | ----------- | ----------- | -----------| ----------- |  ----------- | ----------- |
| Joe | Smith | jsmith@someemail.com| ... | 1 | 2 | 3 |
| Jack | D | jackd@someemail.com| ... | 2 | 3 |1 |
| Betty | Timb | bettytimb@someemail.com| ... | 3 | 1 | 2 |


A elections can be on the same csv. So a ballot combining the top two would look like: 
| First name | Last Name  | Email  | OTHER ELECTION DATA | Rank for canidate -Jane Doe | Rank for canidate -John Doe |  Rank for canidate -Betty White |  Vote on "position name" |
| ----------- | ----------- | ----------- | -----------| ----------- |  ----------- | ----------- | ----------- |
| Joe | Smith | jsmith@someemail.com| ... | 1 | 2 | 3 |  Jane Doe |
| Jack | D | jackd@someemail.com| ... | 2 | 3 | 1 | Jane Doe |
| Betty | Timb | bettytimb@someemail.com| ... | 3 | 1 | 2 |  John Doe |

### Running: 
To run the code: 
'python general.py'
(must be python3)


## Code Elements: 
### Email parsing: 
One functionality of the code is parsing through emails and reporting back on emails without a certain email domain address and repeated emails. In input.py, the decision to count these votes can be decided in ELECTION_DATA (see comments)

