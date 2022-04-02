from SeleniumBot import RedbButtom
from finder import finder
import cryptography
if __name__ == "__main__":
    user_mail, servicios = finder(107551)
    pj = RedbButtom(user_mail)
    pj.forgot()

    