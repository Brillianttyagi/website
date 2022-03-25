from utility.twofactorauth import twoFactorAuth


def account_register(intent,mobile,user,otp):
    twoFactorAuth(mobile,otp)
def account_forget(intent,mobile,user,otp):
    twoFactorAuth(mobile,otp)
def account_sendOtpLogin(intent,mobile,user,otp):
    twoFactorAuth(mobile,otp)
def account_sendMobileOtp(intent,mobile,otp):
    twoFactorAuth(mobile,otp)
