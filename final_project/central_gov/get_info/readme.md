using the csv I got from get_link, I will scrape for two files:
  1. leader.info file that contains basic information such as
    
    -name
    
    -url
    
    -picture_url: url to a photo of theirs
    
    -short_bio
    
    -gender
    
    -ethnic
    
    -dob_y: year of birth
    
    -dob_m: month of birth
    
    -age: 2018 - dob_y
    
    -join_work_y: which year they joined workforce
    
    -working_y: 2018 - join_work_y
    
    -pob: place of birth
    
    -pob_p: province of birth
    
    -join_party_y: which year they joined the CCP, if at all
    
    -edu_dg: their highest degree
    
    -edu_am: education background
    
    -edu_uni: which university they graduated from
    
    -edu_major: major they pursued
    
    -published_date: when was their info published and who published it (人民,新华,etc)
    
    -current_status: current position, including party delegation position
    
    -additional_info: anything else
    
  2. leader.resume file that contains information of ... well, each person's resume:
  
    -name
    
    -year: a range of years
    
    -content: what they were doing where
    
    -url
