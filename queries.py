# This file containes list of queries and needs string formatting

# 
# no paraeters in mockup_1_2
mockup_5 = """
WITH extract_year AS (
    select extract(YEAR from decision_date) AS decision_year
    from visa
),

count_of_app AS (
    SELECT COUNT(ids) as visa_people
    from applicant
    where case_status = 'Certified'
)

select p.year as year, (cp.visa_people/p.midyear_population)*100000 as value
from pop p, applicant a, visa v, extract_year y, count_of_app cp
where p.countries = a.country_of_citzenship and v.ids = a.ids and p.countries = '{0}'
and a.case_status = 'Certified' and y.decision_year = p.year and (p.year >= {1} AND p.year <= {2})
group by p.midyear_population,p.year, cp.visa_people
order by p.year""" 


login = """SELECT count(*) FROM  Login_credentials 
WHERE USER_NAME = '{0}' AND PASSWORD = '{1}'"""

register = """INSERT INTO Login_credentials VALUES ('{0}', '{1}')"""



# records_count = """
# SELECT  (SELECT COUNT(*) FROM APPLICANT) + 
#         (SELECT COUNT(*) FROM SECTOR) +
#         (SELECT COUNT(*) FROM JOB) +
#         (SELECT COUNT(*) FROM VISA) +
#         (SELECT COUNT(*) FROM EMPLOYER) +
#         (SELECT COUNT(*) FROM POP) +
# FROM Dual"""











