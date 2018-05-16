# Auto Login

<center>자동 로그인 과정</center>

```
참고 팀페이지 주소
http://blog.naver.com/PostView.nhn?blogId=pcmola&logNo=220691921068&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
```


### Step 1: Open a terminal session and edit inittab file.
  - : sudo nano /etc/inittab
  
### Step 2: Disable the getty program.
  - : And add a # at the beginning of the line to comment it out
  - : #1:2345:respawn:/sbin/getty 115200 tty1

### Step 3: Add login program to inittab.
  - : Add the following line just below the commented line
  - : 1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1

### Step 4: Save and Exit.
  - : Press Ctrl+X to exit nano editor followed by Y to save the file and then press 
  - : Enter to confirm the filename.


#### <center>또는 라즈베리파이3 에서는 명령어 한 줄로 위의 과정이 생략 가능 </center>
  - : $sudo raspi-config > 3. Boot Options > B2. Console Autologin  
