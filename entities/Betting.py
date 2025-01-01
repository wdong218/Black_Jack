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
    def betting_manage(self,winner):
        if winner:
            self.asset.set_asset(self.current+500)
            self.current = 0
        else:
            q = -self.current
            self.asset.set_asset(q)
            self.current = 0

    # 베팅 금액 반환
    def get_betting(self):
        return self.current
