from SeleniumBot import TwitterBot
import cryptography
if __name__ == "__main__":
    import random
    import string

    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        result_str = ''.join(random.choice(letters) for i in range(length))
        #print("Random string of length", length, "is:", result_str)
        return result_str
    get_random_string(12)
    pj = TwitterBot("leacrigas@outlook.com")
    pj.forgot()

    