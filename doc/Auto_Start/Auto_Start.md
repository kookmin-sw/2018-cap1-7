# Run a Script after login

<center>자동 실행 과정</center>

```
참고 팀페이지 주소
- http://blog.naver.com/PostView.nhn?blogId=pcmola&logNo=220691921068&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

- http://youagain.tistory.com/5

- http://hochulshin.com/python-automatic-run-ubuntu/

- http://fishpoint.tistory.com/2370

```


### Step 1: Open a terminal session and edit the file /etc/profile
  - : sudo nano /etc/profile
  
### Step 2: Add the following line to the end of the file
  - : . /home/pi/your_script_name.sh(점을 찍어야 한다)
  - : replace the script name and path with correct name and path of your start-up script.

### Step 3: Save and Exit
  - : Press Ctrl+X to exit nano editor followed by Y to save the file.



<center>자동 실행 과정2 - rc.local 이용</center>
  
### 참고: http://fishpoint.tistory.com/2370


<img src="/doc/Auto_Start/auto_login.png" width="600px" height="100px">
