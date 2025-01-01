class player:
    def __init__(self):
        self.player_card = []  # 플레이어의 카드 리스트
        self.player_score = 0  # 플레이어의 점수 (계산된 값)

    def get_player_card(self):
        """플레이어의 카드 리스트 반환"""
        return self.player_card

    def add_player_card(self, card):
        """카드를 추가하고 점수를 동적으로 계산"""
        self.player_card.append(card)
        self.player_score = self.calculate_score()  # 전체 점수 재계산

    def get_player_score(self):
        """플레이어의 점수 반환"""
        return self.player_score

    def calculate_score(self):
        """전체 카드 리스트를 기반으로 점수 계산"""
        score = 0
        ace_count = 0

        for card in self.player_card:
            if "A" in card:
                score += 11
                ace_count += 1
            elif "J" in card:
                score += 10
            elif "K" in card:
                score += 10
            elif "Q" in card:
                score += 10
            else:
                if len(card) == 3:
                    score += int(card[:2])
                else:
                    score += int(card[0])

        # Ace 조정: 점수가 21을 초과할 경우 11을 1로 변경
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1

        return score
