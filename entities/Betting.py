from ui.asset import Asset
from sound.SoundManage import SoundManage
class Betting:
    def __init__(self):
        self.current = 0
        self.asset = Asset()
        self.soundmanage = SoundManage()

    # 현재 금액과 비교해 누를때마다 베팅 금액 상승
    def betting_up(self):
        self.soundmanage.up_down_sound()
        if self.current < self.asset.get_asset():
            self.current += 100

    def betting_down(self):
        self.soundmanage.up_down_sound()
        if self.current > 0:
            self.current -= 100
        #누를때마다 베팅 금액 감소
    def betting_manage(self,winner): #게임 스크린에서 승리한 숫자를 받아 베팅 금액에 따라 재산 증가
        #승리
        if winner == 1:
            self.asset.set_asset(self.current+500) #500원은 승리 보너스
            self.current = 0
        #패배
        elif winner == 2:
            q = -self.current
            self.asset.set_asset(q)
            self.current = 0
        #비겼을때
        else:
            self.current = 0

    # 베팅 금액 반환
    def get_betting(self):
        return self.current
