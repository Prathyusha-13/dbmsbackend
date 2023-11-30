# This file containes list of queries and needs string formatting

# 
# no paraeters in mockup_1_2

mockup_1 = """SELECT
    EXTRACT(YEAR FROM V.DECISION_DATE) AS Visa_Year,
    S.ECONOMIC_SECTOR AS Economic_Sector,
    J.WORK_STATE AS Work_State,
    COUNT(*) AS Immigrant_Count
FROM
    APPLICANT A
JOIN
    VISA V ON A.CASE_NO = V.CASE_NO
JOIN
    JOB J ON A.JOB_ID = J.ID
JOIN
    SECTOR S ON J.NAICS_CODE = S.NAICS_CODE
WHERE
    EXTRACT(YEAR FROM V.DECISION_DATE) BETWEEN {0} AND {1}
    AND S.ECONOMIC_SECTOR = '{2}'
    AND J.WORK_STATE = '{3}' 
GROUP BY
    EXTRACT(YEAR FROM V.DECISION_DATE),
    S.ECONOMIC_SECTOR,
    J.WORK_STATE
ORDER BY
    EXTRACT(YEAR FROM V.DECISION_DATE), S.ECONOMIC_SECTOR, COUNT(*) DESC"""

mockup_2 = """
SELECT
    EXTRACT(YEAR FROM V.DECISION_DATE) AS Visa_Year,
    S.ECONOMIC_SECTOR AS Economic_Sector,
    J.PW_LEVEL AS Skill_Level,
    AVG(A.WAGE_OFFERED) AS Average_Wage
FROM
    APPLICANT A
JOIN
    VISA V ON A.CASE_NO = V.CASE_NO
JOIN
    JOB J ON A.JOB_ID = J.ID
JOIN
    SECTOR S ON J.NAICS_CODE = S.NAICS_CODE
WHERE
    EXTRACT(YEAR FROM V.DECISION_DATE) BETWEEN {0} AND {1}
    AND S.ECONOMIC_SECTOR = '{2}'
    AND J.PW_LEVEL = '{3}'
GROUP BY
    EXTRACT(YEAR FROM V.DECISION_DATE),
    S.ECONOMIC_SECTOR,
    J.PW_LEVEL
ORDER BY
    EXTRACT(YEAR FROM V.DECISION_DATE), S.ECONOMIC_SECTOR, J.PW_LEVEL"""

mockup_3 = """
SELECT 
    EXTRACT(YEAR FROM V.DECISION_DATE) AS Visa_Year,
    J.PW_JOB_TITLE AS Job_Title,
    J.PW_LEVEL AS Skill_Level,
    COUNT(A.CASE_NO) AS Foreign_Workers_Count
FROM 
    APPLICANT A
JOIN 
    VISA V ON A.CASE_NO = V.CASE_NO
JOIN 
    JOB J ON A.JOB_ID = J.ID
WHERE 
    EXTRACT(YEAR FROM V.DECISION_DATE) BETWEEN {0} AND {1}
    AND J.PW_JOB_TITLE = '{2}'
    AND J.PW_LEVEL = '{3}'
GROUP BY 
    EXTRACT(YEAR FROM V.DECISION_DATE), J.PW_JOB_TITLE, J.PW_LEVEL
ORDER BY 
    EXTRACT(YEAR FROM V.DECISION_DATE), COUNT(A.CASE_NO) DESC"""

mockup_4 = """
SELECT
    EXTRACT(YEAR FROM V.DECISION_DATE) AS Visa_Year,
    SUM(CASE WHEN V.CLASS_OF_ADMISSION IN ('H-1B', 'H-1B1') THEN 1 ELSE 0 END) AS H1B_Count
FROM
    VISA V
WHERE
    EXTRACT(YEAR FROM V.DECISION_DATE) BETWEEN {0} AND {1}
GROUP BY
    EXTRACT(YEAR FROM V.DECISION_DATE)
ORDER BY
    EXTRACT(YEAR FROM V.DECISION_DATE)""" 

mockup_5 = """
SELECT EXTRACT(YEAR FROM V.DECISION_DATE) AS Visa_Year,
    COUNT(V.CASE_NO) AS Total_Cases,
    SUM(CASE WHEN A.CASE_STATUS = 'Certified' THEN 1 ELSE 0 END) AS Certified_Cases,
    CASE 
        WHEN COUNT(V.CASE_NO) > 0 THEN ROUND((SUM(CASE WHEN A.CASE_STATUS = 'Certified' THEN 1 ELSE 0 END) * 100.0 / COUNT(V.CASE_NO)), 2)
        ELSE 0
    END AS Approval_Percentage
FROM 
    VISA V
JOIN 
    APPLICANT A ON V.CASE_NO = A.CASE_NO
JOIN 
    COUNTRY C ON A.COUNTRY_OF_CITIZENSHIP = C.COUNTRY_NAME
WHERE 
    C.COUNTRY_NAME = '{0}' AND 
    EXTRACT(YEAR FROM V.DECISION_DATE) BETWEEN {1} AND {2}
GROUP BY 
    EXTRACT(YEAR FROM V.DECISION_DATE), C.COUNTRY_NAME
ORDER BY 
    EXTRACT(YEAR FROM V.DECISION_DATE)""" 


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











