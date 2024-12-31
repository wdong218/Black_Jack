class Asset:
    def __init__(self):
        """
        Asset 초기화
        file_path: 재산 정보를 저장할 파일 경로
        """
        self.file_path = "Asset"
        self.balance = 0  # 초기값 0, 파일에서 읽어옴
        self.load_asset()

    def get_asset(self):
        """현재 재산 반환"""
        return self.balance

    def set_asset(self, new_balance):
        """
        새로운 재산 값 설정
        new_balance: 설정할 새로운 재산 값
        """
        self.balance += new_balance
        self.save_asset()

    def load_asset(self):
        """파일에서 재산 정보를 읽어옴"""
        try:
            with open(self.file_path, "r") as file:
                self.balance = int(file.read().strip())
        except FileNotFoundError:
            # 파일이 없을 경우 초기값으로 설정
            print("재산 정보 파일이 없습니다. 초기값으로 설정합니다.")
            self.balance = 10000
            self.save_asset()
        except ValueError:
            print("파일 내용이 올바르지 않습니다. 초기값으로 설정합니다.")
            self.balance = 10000
            self.save_asset()

    def save_asset(self):
        """재산 정보를 파일에 저장"""
        with open(self.file_path, "w") as file:
            file.write(str(self.balance))
