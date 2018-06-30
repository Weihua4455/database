here I cleaned the info and resume files:

for info, I cleaned strings, deleted republicates, and got information such as:
  
  -gender

  -ethnic

  -dob_y: year of birth

  -age: 2018 - dob_y

  -join_work_y: which year they joined workforce

  -pob: place of birth

  -pob_p: province of birth

  -join_party_y: which year they joined the CCP, if at all

  -edu_dg: their highest degree

  -published_date: when was their info published and who published it (人民,新华,etc)

for resume, I pull ["location"] from ["content"], which can be used later for mapping. I also filled time series so each person has a continuous timeline
