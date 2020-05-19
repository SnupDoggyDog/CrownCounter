import re
import os
import sys
import time

def exit_out():
    """
    Fashionably exits the code after a delay
    """
    print("Exiting...")
    time.sleep(3)
    os.system("pause")

try:
    import requests
except Exception:
    print("Module requests was not installed")
    exit_out()

accountList = None
try:
    with open("accounts.txt") as accFile:
        accountList = accFile.read().split("\n")
except:
    print("No accounts.txt was found.\nTry creating a folder called \"AnyNameHere\"\n"
          "Then add an accounts.txt containing accounts")
    exit_out()

FORMAT_ERROR = -1
LOGIN_ERROR = -2

def findTotal(account, numAttempts = 1):
    """
    Finds crown count of a given account\n
    Input: "User:Pass"
    :type account: str
    """
    with requests.Session() as connection:
        accountData = account.split(":")
        if len(accountData) != 2:
            print("Found an incorrectly formatted line in accounts.txt")
            return FORMAT_ERROR
        loginData = {
            'userName': accountData[0],
            'password': accountData[1],
            't:formdata': 'H4sIAAAAAAAAAJXRvUoDQRAH8E0wEkiniPiFFrHda0yhNqYRxUOEEAu7vdvxsslmd93Z804LW9/CJxBrrVPY+Q4+gG0qC/cCEeQkYrMLwzDz4z+PH6SWbZINlrpekIlbZnkQ6kSoPQtcWIhdaiVacqBtQplhcQ+oYwbQ2ZsWjbUFKSL/D41WoBzSI8E5qOaZ1TEgdtJoKBCFVhf3W4v52vN8lVRC0oi1clbLUzYERxbCPrtmgWQqCTrOCpXs58aRxlTQtTJbJ6tlYopglR/hfa2Zvogh0Hbkiyx2hwIkb3bApWa7O2q8L71+llBX5I5UCkS92FFU/hS0/ysoRTR64juX44e3KiG5+X2fYYiZthwL4JznTQuz24vuerZClsstsng9f9ffkA589ihQAs3gx1UnSBcKNSizX04G/fNQjSch1lwPjvl3fLXJ+C8uOCzhZQIAAA=='
        }
        url = "https://www.wizard101.com/auth/wizard/login.theform"
        connection.post(url, data = loginData)
        newUrl = "https://www.wizard101.com/user/kiaccounts/summary/game?context=am"
        testData = connection.get(newUrl)
        try:
            rawText = str(testData.content)
            crownsData = re.search("\"crownsbalance\"><b>(([0-9]*,)*([0-9]*))", rawText)
            result = crownsData.group(0)
            crownsTotal = result[19 : len(result)]
            return int(crownsTotal.replace(',', ''))
        except Exception:
            if numAttempts < 3:
                print("Couldn't log into %s. User/Pass was invalid or a captcha must be done on wizard101.com" % accountData[0])
                print("Continue when finished with the captcha")
                os.system("pause")
                return findTotal(account, numAttempts = numAttempts + 1)
            else:
                print("Failed login. Moving on to next account...")
                return LOGIN_ERROR

if __name__ == '__main__':
    allCrowns = 0
    outputText = ""
    pack_199 = 0
    pack_299 = 0
    pack_399 = 0
    pack_599 = 0
    energy_elixir = 0

    for account in accountList:
        currTotal = findTotal(account)
        if currTotal == FORMAT_ERROR:
            outputText += ("No data for incorrectly formatted line: %s\n" % account)
            continue
        user = account.split(":")[0]
        if currTotal == LOGIN_ERROR:
            outputText += ("Failed to log into account: %s\n" % user)
            continue
        pack_199 += currTotal // 199
        pack_299 += currTotal // 299
        pack_399 += currTotal // 399
        pack_599 += currTotal // 599
        energy_elixir += currTotal // 250
        allCrowns += currTotal
        printText = ("Account: %s had %i crowns" % (user, currTotal,))
        print(printText)
        outputText += printText + "\n"

    totalText = ("\nTotal: %i" % allCrowns)
    outputText += ("%s\n" % totalText)
    print(totalText)
    purchaseText = ("Purchasable 199 Packs: %i\n299 Packs: %i\n399 Packs: %i\n599 Packs: %i\nEnergy Elixirs: %i"
                    % (pack_199, pack_299, pack_399, pack_599, energy_elixir,))
    print(purchaseText)
    outputText += purchaseText
    print("CrownCounter finished running.")

    with open("output.txt", "w+") as output:
        output.write(outputText)
    exit_out()