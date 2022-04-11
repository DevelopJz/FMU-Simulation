# Python3 연습 과제
## 4-Python3 FMU-Simulation

### 사용 언어
**Python 3.7.6**  
**Anaconda 4.8.2**

### 사용 환경
**Windows**

### 라이브러리
__future__  
csv  
numpy  
fmpy  
sys  

### 라이브러리 설치
```python

python -m pip install 라이브러리명

```

### 코드 설명
**fmuinfo_make.py**  
동역학 시뮬레이션 프로그램 Dymola의 모델 파일 FMU 파일을 읽고 파일의 정보를 txt파일로 저장  

**fmpy_input_test.py**  
fmuinfo_make.py 로 만든 fmu_info.txt파일을 읽어 FMU 파일에 input.csv 파일을 넣고 시뮬레이션 하여 output.csv 파일 출력  
시뮬레이션 결과 그래프 저장  

**result**  
![image](https://user-images.githubusercontent.com/96412126/162850569-2648e680-288f-430d-93d5-d331c53ecd99.png)
