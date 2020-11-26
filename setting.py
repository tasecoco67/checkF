import os
from dotenv import load_dotenv

# .envファイルの内容を読み込みます
load_dotenv()

IUR = os.environ.get("INURL")
TWR = os.environ.get("TWURL")
NUR = os.environ.get("NTURL")
NUR2 = os.environ.get("NTURL2")
MAIL = os.environ.get("MAIL")
PSW = os.environ.get("PSW")
NUR3 = os.environ.get("NTURL3")
SPK = os.environ.get("SPREADSHEET_KEY")
CEMAIL = os.environ.get("CEMAIL")
CID = os.environ.get("CID")
CCU = os.environ.get("CCU")
PKI = os.environ.get("PKI")
PK = os.environ.get("PK")
