import smtplib

try:
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.starttls()
        smtp.login('ning@novele.com', 'Yeezy20220701!')
        print("✅ SMTP login success，you are able to send emal now")
except Exception as e:
    print("❌ login failed：", e)
