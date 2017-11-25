# WebCrawler_Learn
>2017.11.22
>>Create repository.
>>Add "main.py".
>
>2017.11.26
>>New Crawler "main_proxies.py".
>>New module "SendMail".
>>Modify old Crawler and rename to "main_acm".
>>"main_acm" can save the images to the folder in this project now.

------------------------
## main_acm
    This Crawler can get all the profile picture of users from https://acm.bitnp.net.<br>  
    Unfortunately,there are some problems: The style of code is still terrible and lack comments.<br>  
    Maybe they could be solved at next update.
    
## main_proxies
    This Crawler can get all the proxies-ip from https://www.kuaidaili.com.
    
## SendMail
    This module can send email by smtp server.<br>   
    There are two function in it: login(stmp_address,stmp_port,From_address,password) and sendmail(To_address,subject,content,attachment_address(or not)). Exemple:<br>   
    ```python
    import SendMail
    SendMail.login('smtp.163.com', 25, 'xxxxxxx@163.com', '*********')
    SendMail.sendmail('xxxxxxxx@gmail.com', 'Text', 'Hello,by Python', 'E:\hello.txt')
    SendMail.sendmail('xxxxxxxx@foxmail.com', 'Text2', 'Hello,by Python')
    ```
