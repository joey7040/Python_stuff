class validator:

    def user_is_valid(self, username):
        if len(username) > 10:
            return False

        if ' ' in username:
            return False

        if username.islower():
            return False

        return True


if __name__ == '__main__':
    validator.user_is_valid()
