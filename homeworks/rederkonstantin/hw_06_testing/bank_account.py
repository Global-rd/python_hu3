
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):       # Vizsgálat, hogy a target account az szám-e?
            raise TypeError("Target must be a number. (int, float)")            # Ha nem, akkor aztán speciálisra szabott üzenet.
        if balance < 0:                                                         # ha netán az induló ballance nullánál kevesebb lenne, error van .....
            raise ValueError("Initial balance cannot be negative.")             # egy jó öreg ValueError saját szöveggel.
        balance 
        self.owner = owner              # a tulajdonos neve
        self.balance = balance          # aktuális pénz mennyiség
    
    def deposit(self, amount: float):
        """
        Increases ballance with amount.
        Input: amount:float.
        """
        if amount <= 0:                 # Ellenőrzés, ha nulla, vagy negatív, akkor error van. Nullának nincs értelme, a mínusz meg nem deposit....
            raise ValueError("Deposit amount must be positive.") # Saját szöveg: A befizetés csak pozitív lehet, nullának sincs értelme...
        self.balance += amount          # Itt meg jól megnöveljük a balance-ot a befizetéssel.
    
    def withdraw(self, amount: float):
        """
        Decreases ballance with amount.
        Input: amount:float.
        """
        if amount <= 0:                 # A pénz kivét is csak pozitív szám lehet.
            raise ValueError("Withdraw amount must be positive.")   # Újabb speciálisra szabott hibaüzenet.
        if amount > self.balance:       # Itt már arra figyelünk, hogy csak annyit tudunk kivenni pénzt, amennyi a számlán van.
            raise ValueError("Insufficient funds.")                 # Újabb speciálisra szabott hibaüzenet.
        self.balance -= amount          # Itt meg jól lecsökkentjük a balance-t a kivett összeggel.

    def transfer(self, amount: float, target_account: 'BankAccount'):
        """
        Transfer money from account to another account.
        Input:
            amount: amount of transfer:float
            target_account: account of destination of money: BankAccount:Class
        """
        if not isinstance(target_account, BankAccount):     # Vizsgálat, hogy a target account az BankAccount Class-e?
            raise TypeError("Target must be a BankAccount instance.")   # Ha nem, akkor aztán speciálisra szabott üzenet.
        
        if target_account == self:
            raise ValueError("Money sending to yourself is increase margin of Bank. They have enought. :)")

        self.withdraw(amount)           # Ha van célaccount, akkor a withdraw -al levonjuk az összeget,
        target_account.deposit(amount)  # majd a célaccount balance-át jól megnöveljük az összeggel, ha el nem megy az áram. :)
    
    def get_balance(self):              # Ha netán valaki kíváncsi az aktuális balance-ára, 
        return self.balance             # Akkor vissza adjuk neki az információt.

    def __str__(self):                  # Itt meg segítünk mindenkinek, hogy ha kiprinteli az objektumot, ne legyen kínai....
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
    
def main():                             # Fő hurok
    Golyó = BankAccount("Golyó", 2000.0)
    Koni = BankAccount("Koni", "2000" )
    print(Golyó)
    print(Koni)
    
if __name__ == "__main__":              # Ez meg, ha máshol használják majd, ne gengszterkedjenek a tesztügyek.
    main()