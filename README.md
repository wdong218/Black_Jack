# Black_Jack



🃏 블랙잭 게임 구현 프로젝트

프로젝트 설명

목표
블랙잭 게임을 구현하며 Git 사용법과 브랜치 전략을 연습합니다.

Jira를 활용해 스프린트 계획 및 태스크 관리를 통해 협업 프로세스를 익히는 것을 목표로 합니다.

상세 프로젝트 개요

프로젝트의 전체 개요는 [Notion 링크](https://www.notion.so/16226275352480c6accfdea53f38e27d?pvs=4)에서 확인할 수 있습니다.

🎯 게임 룰

게임 목표

21에 가장 가까운 카드 합을 가진 플레이어가 승리합니다.

카드 합이 21을 초과하면 즉시 패배합니다.

카드 값:

숫자 카드 (2~10): 카드에 적힌 숫자 그대로.

그림 카드 (J, Q, K): 10점.

에이스 (A): 1점 또는 11점 (유리한 값으로 자동 계산).

게임 진행

1. 베팅 시작: 플레이어는 딜러와 게임하기 전 베팅 금액을 설정합니다.

2. 행동 선택:

Hit: 카드를 한 장 더 받습니다.

Stand: 현재 카드로 게임을 유지합니다.

3. 딜러의 턴:

Stand 후 딜러의 턴이 시작됩니다. 

딜러는 카드 합이 17 이상이 될 때까지 카드를 받습니다.

4. 승패 판정:

21 초과: 해당 플레이어는 패배합니다.

더 높은 점수: 카드 합이 더 높은 쪽이 승리합니다.

💻 개발 목표

1. 기본 게임 기능:
   
- 카드 배분, 행동 선택 (Hit, Stand 등), 점수 계산 로직 구현.

3. 사용자 인터페이스 (UI):
- 게임 화면 구성: 플레이어와 딜러의 카드 및 점수 표시.
- 버튼 UI: Hit, Stand 버튼 추가.
- 상태 표시: 현재 점수와 게임 상태를 표시하는 영역 구성.

4. 시각적 이미지 추가:

- 배경화면: 도박장 느낌의 디자인.
- 카드 이미지: 각 카드에 맞는 이미지를 적용.

5. 베팅 시스템:
- 게임 시작 시 베팅 금액 설정 기능.
- 승패에 따라 베팅 금액 증감 처리.
- 게임 도중 베팅 변경 시 경고 메세지 출력

6. 사운드 추가:
- 배경 음악 및 효과음 추가.
- 승패시 효과음 추가.

📽️ 게임 플레이 영상



https://github.com/user-attachments/assets/22185ced-bbdb-41d5-a3f0-20ee8ad9cf3a



## 🔧 **사용법**

### 1. **프로젝트를 클론합니다**
```bash
git clone https://github.com/wdong218/Black_Jack.git
```

## Pygame 모듈 설치

### Mac 사용자의 경우

```bash
# Python이 설치되어 있는지 확인합니다.
python3 --version

# 설치되어 있지 않다면 Python 공식 웹사이트에서 Python을 설치하세요.

# pip를 사용해 Pygame을 설치합니다.
python3 -m pip install pygame
```
### Window 사용자의 경우
```bash
# Python이 설치되어 있는지 확인합니다.
python --version

# 설치되어 있지 않다면 Python 공식 웹사이트에서 설치할 때 "Add Python to PATH" 옵션을 체크하세요.

# pip를 사용해 Pygame을 설치합니다.
pip install pygame
```
## 게임 실행방법
### Mac 사용자의 경우
```bash
# 프로젝트 디렉토리로 이동합니다.
cd Black_Jack

# 게임을 실행합니다.
python3 main.py
```
### Window 사용자의 경우
```bash
# 프로젝트 디렉토리로 이동합니다.
cd Black_Jack

# 게임을 실행합니다.
python main.py
```

🗂️ 프로젝트 구조

```plaintext
Black_Jack/
├── assets/
│   ├── background_image/    # 배경 이미지 파일
│   ├── card_image/          # 카드 이미지 파일
│   ├── font/                # 폰트 파일
│   └── sounds/              # 사운드 파일
├── core/
│   ├── Card.py              # 카드 클래스
│   ├── Deck.py              # 카드 덱 관리
│   ├── game_screen.py       # 게임 화면 관리
│   └── GameManager.py       # 게임 진행 로직
├── entities/
│   ├── Betting.py           # 베팅 관련 클래스
│   ├── dealer.py            # 딜러 클래스
│   └── player.py            # 플레이어 클래스
├── sound/
│   └── SoundManage.py       # 사운드 관리 모듈
├── ui/
│   ├── asset.py             # UI 에셋 관리
│   └── button.py            # 버튼 UI 구성
├── main.py                  # 게임 실행 파일
└── README.md                # 프로젝트 설명 파일
```

🙌 기여 방법

이슈를 확인하고 해결하고 싶은 항목을 선택하세요.
feature/기능명 브랜치를 생성하고 작업합니다.
PR을 생성하고 코드 리뷰를 받으세요.
