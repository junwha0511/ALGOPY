# Ⅰ. 활동 목적 및 계획
##   1. 활동 목적
  혼자 수학 문제를 끙끙거리는 것보다는 친구들과 함께 방향을 탐색하며, 개념을 탐색하며 푸는 것이 더 학습에 도움이 되었고, 기억에 깊게 남아 학습에 큰 도움이 되었다. 이렇게 친구들과 수학 문제를 풀 때, 또는 과학에 대한 개념을 바로 잡을 때 집단 지성이 발휘된다.    또한 이때 발휘된 집단 지성은 혼자 학습하는 것보다 매우 뛰어난 학습 효율을 가져다준다. 하지만 함께 학습하는 것이 때로는 학습에 방해가 될 때도 있다. 다른 친구와 생각이 맞지 않아 학습과는 관련이 없는 일로 논쟁을 벌이거나, 학습이 아닌 다른 곳으로 이야기가 빠지는 경우가 그 대표적인 예이다. 알고리즘 문제의 해결에 있어서는 집단 지성이 매우 적합한 학습 방법이다. 집단 지성을 통해 새로운 개념을 탐색하고, 방향성을 제시하며 즐겁게 문제를 풀어나갈 수 있으며, 수학 문제를 같이 풀 때의 기쁨을 알고리즘에서도 느낄 수 있다. 프로그래밍의 학습 역시 집단 지성이 중요하기에 이렇게 집단 지성을 활용한 활동을 기획하게 되었다.

##   2. 활동 계획
###     1)파이썬(Python)의 사용
파이썬의 대표적인 철학 세 가지는 다음과 같다.

> Beautiful is better than ugly
> 아름다운 것이 추한 것보다 낫다

> Explicit is better than implicit
> 명시적인 것이 암시적인 것보다 낫다

> Simple is better than complex
> 간결한 것이 복잡한 것보다 낫다

이 세 가지 철학을 포함한 20개의 철학을 바탕으로 만들어진 파이썬은 다른 언어들에 비해 간결하고, 명시적이며 아름다운 코딩 형식을 가지고 있다. 대표적인 차이로 대부분의 프로그래밍 언어가 가지고 있는 문장 끝의 새미콜론이 없고, 중괄호가 존재하지 않는다.
모든 구분을 공백과 줄 바꿈으로 표현한 파이썬이야 말로 1bit의 차이가 프로그램의 질을 좌우했던 20세기와 달라진 21세기를 대표하는 언어라고 할 수 있다.
 파이썬은 코드를 한줄 씩 해석하는 인터프리트 형식의 언어로, 수학에 관련된 라이브러리가 풍부하며 최근 인공지능, 웹, 데이터 처리 등에 사용되고 있다.
 이러한 특성들 덕분에 파이썬은 처음 프로그래밍을 배우는 사람이 입문하기 쉽고, 확장성이 넓으며, 다양한 분야에서 활용될 수 있다. 그렇기 때문에 앞으로의 부원들의 삶에도, 배우기에도, 알고리즘 문제를 풀기에도 적합한 언어라고 생각하였고, 파이썬을 동아리의 중심 언어로 선정하게 되었다.

##     2)학습 및 활동 계획
 초기에는 동아리장이 직접 부원들에게 강의하려고 계획하였지만, 프로그래머스에서 좋은 인터넷 강의를 발견해 강의의 커리큘럼을 따라가기로 계획하였다.
 월별로는 3월과 4월에 파이썬을 프로그래머스(http://programmers.co.kr/learn/courses/2)에서 학습하고 5월부터 백준과 더블릿, 코드업에서 문제 두 개를 설정해 두 조로 나뉘어 풀기로 계획하였다. 6월에는 그 동안 나온 NYPC 기출 문제를 푼 뒤 NYPC에 출전하기로 계획하였다.


# Ⅱ. 활동 과정
##   1. 장소 선정
 부원이 모두 기숙사 학생이라는 점, 컴퓨터를 쓸 수 있어야 하는 장소여야 한다는 점을 고려해 기숙사 내 4번 학습실로 활동 장소를 선정하였다. 매주 목요일 아침과 화요일 아침에 활동하려고 계획하였지만. 기숙사에서 아침 자율동아리 활동을 주 1회만 허용하는 정책을 실행하여 월요일 아침에는 2학년 3반 교실에서, 목요일 아침에는 기숙사 4번 학습실에서 학습을 진행하게 되었다. 6월에는 수요일에 휴일이 많아 목요일 아침에도 2학년 3반에서 활동하였다.

##   2. 학습 과정
###     1)파이썬 학습
     (1)REPL(Read-Eval-Print Loop)
  REPL은 프로그래밍 언어를 한 줄씩 입력해 한 줄씩 결과를 살펴볼 수 있는 방식으로 파이썬의 특징 중 하나라고 할 수 있다. REPL은 Windows의 Powershell, Linux의 Terminal과 같은 CLI(Commend-Line user Interface)에서 실행되며, 자신이 프로그래밍 한 결과를 바로 확인할 수 있기 때문에 오류 수정이나 간단한 계산에 용이하다.	

     (2)print 함수
 print 함수는 print(“”) 또는 print(‘’)에서 작은따옴표나 큰 따옴표 안에 있는 문자들을 문자열로 인식해 그대로 출력한다. 파이썬의 print 함수는 기본적으로 줄 바꿈을 제공하는데, 줄 바꿈을 제거하기 위해서 print(“”, end=“”) 형식을 사용할 수 있다.

     (3)변수
 변수는 수학에서 사용하는 X처럼 임의의 문자를 정해 그 안에 값을 저장하는 것이다. 보통 프로그래밍 언어에서는 자료 형을 설정해 그 안에 들어갈 수 있는 자료를 특정해주어야 하지만, 파이썬에서는 변수를 선언할 당시 저장되는 데이터를 인식해 자동으로 자료 형을 지정한다. 따라서 변수 선언 방법은 다음과 같다.
 변수 명 = 값

 (2)의 print 함수에서 변수를 출력하려면 print(변수 명)으로 간편하게 출력하는 방법도 있지만 %d(10진수), %f(실수), %s(문자열) 등의 서식 문자를 이용해 print(“서식문자”% 변수 명)의 형식으로 출력할 수 있다. 전자는 자바의 형식에 가깝고, 후자는 C의 형식에 가깝지만, 자바 역시 C의 방식을 호환하기 때문에 전자가 더 발전한 방식임을 확인 할 수 있다.

     (4)주석
 다른 사람에게 프로그래밍 한 코드를 보여줄 때, 또는 수 백 줄이 넘어가는 코드를 자신이 다시 볼 때 설명이 필요할 수 있다. 이렇게 코드 중간에 설명을 넣어줄 수 있게 하는 것이 주석이다. 파이썬이 인터프리트 될 때 주석은 건너뛰고 인터프리트 한다.  #을 표기한 후 문자를 입력하면 주석이 된다. 여러 줄의 설명이 필요할 때는 큰 따옴표를 문장 양 끝에 세 개씩 넣어주면 된다.

     (5)Visual Code와 Powershell의 사용
 REPL 방식으로 하는 프로그래밍은 전체적인 프로그램을 짜기 힘들고, 한번 작성한 코드가 남지 않는다는 단점이 있다. 그렇기 때문에 보통 프로그래밍을 할 떄는 Microsoft사의 Visual Code와 같은 에디터를 통해 .py를 확장자로 하는 파이썬 코드를 작성한 후 Powershell에서 python 파일명 명령어를 통해 프로그램을 실행한다.
Powershell 명령어로는 폴더를 이동하는 cd, 폴더 내 파일 목록을 보여주는 ls가 대표적이다.

     (6)if문과 else문
 if문과 else 문을 배우기 전에는 값을 입력받아 계산을 하고 출력을 하는 과정 외에 특별히 프로그래밍이라고 할 수 있는 요소가 없다. 하지만 if문과 else문을 배우고 나면 조건에 따라 판단을 할 수 있는 기능을 구현할 수 있기 때문에 알고리즘 문제를 풀기 위해 가장 필수적이고 중요한 학습 요소이다.
 if문과 else 문은 if, elif, else로 나뉜다. 

      (가) 조건식
 if문은 조건식의 참, 거짓 여부에 따라 실행하는 내용이 달라진다.
조건문은 1이 true, 0이 false인 하나의 판별식이다. 종류로는 a<=b, a>=b, a==b, a!=b, or, and가 있으며 두 변수의 대소를 판별하는 기능, 두 변수가 동일한 지 판별하는 기능, 양쪽의 판별식이 모두 참이거나 하나만 참인 것을 판별하는 기능을 수행한다.

      (나) if문
 if 조건식: 
	 실행내용
 if문은 조건식이 참일 때 if문 안의 내용을 실행한다. 이때 주의해야할 점은 조건식이 참일 때 실행할 내용들을 들여쓰기 해야 한다는 것이다. 들여쓰기가 되지 않으면 if문에서 빠져나오는 것이기 때문에 조건식이 참이 아닐 때도 실행된다.

      (다) else문
 if 조건식: 
	 실행 내용 
 else: 
 	 실행 내용 
 else문내의 실행 내용은 if의 조건식이 참이 아닐 때 실행된다.

     (7)함수
 함수는 가독성을 높게 하고 프로그래밍 후 코드를 수정할 때 편리하게 해준다. 
파이썬에서 함수는 다음과 같이 선언한다.

def 함수 명(매개인자1, 매개인자2, ...):
 실행 내용
 return 리턴 값

함수에서는 매개인자들을 받아 실행 내용을 수행 한 뒤 마지막으로 return을 통해 결과를 출력한다.
함수에서 받을 수 있는 매개인자의 개수는 제한이 없으며, return은 생략될 수 있다. 함수를 호출할 때는 함수명(매개인자1, 매개인자2, ...)의 형식으로 호출한다. 

     (8)리스트
 리스트는 특정 열에 새로운 요소를 삽입할 경우, 그 장소를 비우기 위해 요소를 이동시켜야 되는 일반적인 프로그래밍 언어의 배열과는 달리 데이터의 삽입 및 삭제가 빠르다. 데이터와 포인터로 구성된 각각의 기억장소를 노드(node)라고 하는데, 왼쪽엔 데이터 값, 오른쪽은 다음 노드를 나타내는 포인터 값이 들어간다. 마지막 노드의 포인터 값인 NULL은 리스트의 끝을 나타낸다. 보통 코딩을 할 때, 데이터 부분을 element, 포인터 부분을 next로 나타낸다. listhead는 연결 리스트의 첫 노드를 나타내는 포인터로, 이 값을 통해 모든 노드를 참조할 수 있다. 
 연결 리스트는 특정 요소를 참조하기 위해 첫 노드부터 순차대로 조사를 해야 한다. start는 한 요소를 나타내는 포인터 값인데, while 조건문을 이용해 해당 요소까지 찾아가는 과정을 나타낸다.
 또한 쉬운 데이터 삽입과 삭제가 가능한 리스트는 노드와 노드 사이에 새로운 노드를 삽입할 수 있다.
 새로 삽입할 노드를 나타내는 포인터 값 q를 활용하여 다음 그림과 같이 노드를 삽입할 수 있다.

     (9)for문
 for문은 반복적인 작업들을 간단한 코드로 줄여준다. 
for i in range(초기 값, 마지막 값):
	실행내용
의 형식으로 주로 사용되며, i를 반복 변수로 하고 초기 값부터 마지막 값까지 증가시킨다. 따라서 실행내용은 ‘마지막 값-초기 값+1’만큼 실행된다.
    2)알고리즘 문제 해결  
     (1)피보나치 수열
문제: 피보나치 수열을 1항부터 100항까지 나열하세요.
      (가) 해결 방법 탐구
피보나치 수열의 원리는 간단하다. 앞항과 뒷항을 더한 값을 뒷항에 추가해주면 되는 원리이다. 이러한 과정을 코드화하기 위해 초기 값으로 a를 1로, b를 1로 설정하였다. 여기서 a와 b는 인접한 두 항을 의미한다. 또한 temp라는 변수를 사용하여 a의 값을 임시로 저장할 수 있게 하였다.
for문을 통해 반복을 하였지만, i의 값은 사용하지 않았다. temp에 a를 잠시 저장해두고, a에 b를 저장하고, b와 원래 a값을 더해 다시 b에 저장하는 방식으로, 즉 피보나치 수열을 두 항씩 거쳐가며 출력하는 방식으로 프로그램을 작성하였다.
      (나) 느낀 점
 처음으로 풀어보는 문제라 주도적으로 참여하지는 못했다. 하지만 이제 드디어 알고리즘 문제를 풀어볼 수 있다는 사실이 기뻤다. 
 비록 프로그래밍을 배운 후 처음 풀어보는 알고리즘 문제라 집단 지성이 발휘되지는 못했지만, 앞으로 즐거운 활동을 지속할 수 있다는 사실에 가슴이 두근거렸다.

     (2)별 피라미드
문제: 다음과 같이 별 피라미드가 출력되는 프로그램을 작성하세요.
*
**
***
****
*****

      (가) 해결 방법 탐구
for문을 통해 range로 줄의 범위를 지정한 후, 해당 줄의 수만큼의 별을 또 다른 for문으로 출력한다. I를 변수로 하는 for문 안에 있는 for문은 I개의 별을 출력해야하기 때문에 I까지를 반복 범위로 한다.

이때, 파이썬은 기본적으로 print()가 줄 바꿈을 지원하므로 단순히 print()를 하였을 때는 줄 바꿈을 한 것과 마찬가지이지만, print(“”, end=“”)로 마지막 인덱스에 자동으로 추가되는 줄 바꿈 문자‘\n’을 제거해주면 한 줄로 줄 바꿈이 되지 않는다.

      (나) 느낀 점
처음 이 활동을 접하였을 때, 이해되지 않는 부분이 많았다. 하지만, 동아리 부원들과 함께 고민해보며 탐구한 결과 완벽하게 이해할 수 있었다.‘별 피라미드’를 출력하기 위해 코드를 작성할 때, 이전에 생각하지 못한 부분을 많이 발견할 수 있었다. 함께 생각을 나눈 결과 즐겁게 해결할 수 있었으며 앞으로의 활동 또한 부원들과 함께 머리를 맞댄다면 모두 충분히 해결할 수 있을 것이라 생각된다.

     (3)등차수열의 판별
문제: 세 수를 입력 받고 등차수열인지 판별하세요.

      (가) 해결 방법 탐구
 먼저 등차수열을 만들기 위해서 a1, a2, a3, 변수에 input()으로 값을 입력 받는다. 여기서 입력 받을 때, 문자형, 실수형, 정수형 등 다양한 형태로 입력할 수 있으므로 이것을 모두 정수형으로 인식할 수 있도록 int()로 감싸준다. 등차수열의 뒷항에서 앞항을 빼면 공차이므로 두 항의 차로 구한 공차가 서로 같으면 등차수열이다.
  	
따라서 
r1= a2-a1
r2= a3-a2로 두고 만약 r1과 r2가 같으면 등차수열이고 다르면 등차수열이 아니므로 if문과 elif를 사용해 결과를 출력할 수 있다. 

      (나) 느낀 점
 이 활동에서 처음 문제를 듣고 어떻게 해야 할지 모르겠어서 막막했었다. 하지만 그 동안 배우고 연습한 것을 활용해보려 했고 어려운 것을 도움 받아가며 등차수열을 만들어내니 뿌듯하고 그동안에 배웠던 것이 어떻게 쓰이는지 조금은 알 수 있었던 활동이었다. 이 활동을 하고나서 등비수열도 만들어보고 싶다는 생각이 들었고 더 배우고 싶다는 생각이 들게 하는 활동이어서 매우 유익했다고 생각한다.

     (4)등비수열의 판별
문제: 세 수를 입력 받고 등비수열인지 판별하세요.

      (가) 해결 방법 탐구
 저번에 프로그래밍 했던 등차수열 판별하는 문제를 해결한 후, 등비수열도 해보고 싶다는 생각이 들어서 시작하게 되었다. 등차수열과 비슷하게 a1, a2, a3 에 input()으로 값을 입력 받았다. r1 과 r2를 빼기가 아닌 나누기로 하여 r1 = a2/a1, r2 = a3/a2 로 둔 후 if문과 elif를 사용해 ‘등비수열입니다.’와 ‘등비수열이 아닙니다.’를 출력하게 하였다. 


      (나) 문제점 및 해결 방안
 가.와 같은 프로그램을 작성해 테스트를 진행하였으나, 일반적인 1,10,100같은 수는 등비수열로 인식하지만 0.001 0.01 0.1은 등비수열로 인식하지 않는 상황이 발생했다. 그 이유는 프로그래밍에서 부동 소숫점 방식의 표현에서 오차가 조금씩 발생하기 때문이다. 하지만 아직 해결할 방법을 찾지 못했다. 이 문제는 정보선생님과 이야기하며 차후 풀어 나가야 할 문제이다.

      (다) 느낀 점
 이 활동은 직접 호기심을 가지고 시도해본 활동이라 더 의미 있었다. 코딩의 즐거움을 더 느낄 수 있었던 것 같다. 하지만 아직 해결되지 않은 부분이 있어 아쉽기도 했다. 그래도 파이썬이 조금 익숙해져서 뿌듯함을 느낄 수 있었다.


# Ⅲ. 결과 및 차후 활동 계획
##   1. 학습 결과
  초기 계획보다 파이썬의 학습이 더 많은 시간이 걸렸다. 개개인의 습득 속도와 여러 변수들이 있었기 때문이다. 하지만 다행히도 올해 NYPC(Nexon Programming Challenge)가 8월에 열려 안정적으로 계획을 수정할 수 있게 되었다. 
##   2. 활동 결과
 알고리즘 문제를 해결하는 활동을 진행하면서 처음에는 어려움을 겪었다. 생각했던 것처럼 집단 지성이 발휘되지 않았기 때문이다. 수학 문제를 풀 때 발휘 되었던 집단 지성은, 모두가 수학이라는 학문을 공통으로 잘 알고 있기에 가능한 것이었다. 하지만 알고리즘 문제는 성격이 조금 달랐다. 동아리 부원들은 프로그래밍을 막 배운 뒤였고, 바로 프로그래밍 문제를 풀기에는 무리가 있었던 것이다. 그래서 알고리즘 문제가 아닌, 기능을 익히는 쉬운 문제부터 천천히 풀어나가는 시간을 가졌다. 이렇게 하고 나니 조금씩 집단 지성이 발휘되기 시작했다. 그리고 지금은 집단 지성의 꽃이 피고 있다. 앞으로의 활동이 매우 기대된다.

##  3. 차후 활동 계획
###     1)지속적인 알고리즘 문제 풀이
  앞으로의 활동은 백준 사이트와 더블릿 사이트의 알고리즘 문제를 난이도를 점점 높여가며 함께 풀어나가는 활동이 중심이 될 것이다. 

###     2) NYPC 출전 준비
이번 NYPC는 8월 10일부터 8월 31일까지 신청할 수 있으며, 8월 22일부터 8월 31일까지 온라인으로 예선이 진행되고 10월 27일에 본선이 넥슨 본사에서 열린다. 대회 준비를 위해 홈페이지에는 약 30여개의 문제가 공개되어 있기 때문에 7월 중순부터 이 문제들을 차근차근 풀어나가기로 계획하였다.

###     3) 알고리즘 심화 개념
항상 모든 길에는 빠른 길과 느린 길이 있다. 그리고 알고리즘은 여러 개의 길 중 가장 최적화 된, 가장 빠른 길을 찾는 것을 말한다. 따라서 프로그래밍을 갓 배운 집단의 지성을 사용한 문제 풀이만으로는 최적화 된 길을 찾기에 어려움이 있다. 때문에 이번 방학 때, 혹은 2학기 중에 알고리즘 책을 빌려 공동으로 읽고, 책의 내용을 활용할 수 있는 수준으로 지식을 끌어올리려고 한다. 책을 통해 더 빠른 길을 향해 갈 수 있는 발을 얻는 다면 집단의 지성은 상향되어 더욱 위를 바라볼 수 있게 될 것이다.
  



# 참고 문헌
파이썬 철학 (Python Philosophy) https://gist.github.com/Nesffer/30651e6197f03eb029720a0e5b1e0c22

프로그래머스
https://programmers.co.kr/learn

백준 알고리즘
https://www.acmicpc.net/

그림으로 배우는 알고리즘(스기우라 켄)


