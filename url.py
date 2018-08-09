import requests, pytesseract, json
from io import BytesIO
from PIL import Image
from lxml import html

with requests.Session() as s:
    #s.auth({'Login1$UserName': 'tedataview', 'Login1$Password': 'matrix@tedata'})
    r = s.get('https://adsl.te.eg/')
    tree = html.fromstring(r.text)
    vState = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    eValidation = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]



    r = s.post('https://adsl.te.eg/', data = {'Login1$UserName': 'tka', 'Login1$Password': 'tkavoda9090@@',
                                             '__EVENTTARGET': 'Login1$LoginLinkButton', '__VIEWSTATE': vState, '__EVENTVALIDATION': eValidation})

    tree = html.fromstring(r.text)
    vState = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    eValidation = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]
    btnS = ('ابحث')
    #vStateG = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]

    s.get('https://adsl.te.eg/ISP/ISP-tel.aspx')

    im = Image.open(BytesIO(s.get('https://adsl.te.eg/Captcha.ashx').content))
    text = pytesseract.image_to_string(im)
    print(text)
    print (vState)
    print(eValidation)
    data = {'ctl00$ContentPlaceHolderBody$drp_City': '1', 'ctl00$ContentPlaceHolderBody$txt_ClientCircuitNum': '22521277', 'ctl00$ContentPlaceHolderBody$txtVerify': text
            , '__EVENTTARGET': '', '__EVENTARGUMENT': '', '__SCROLLPOSITIONX': '0', '__SCROLLPOSITIONY': '124'
            ,'__VIEWSTATE': vState, '__EVENTVALIDATION': eValidation, '__VIEWSTATEGENERATOR': 'AF0319FB'
            , 'ctl00$ContentPlaceHolderBody$btnAvailabilityRequest': ''}#_D8_A7_D8_A8_D8_AD_D8_AB

    #r = s.send(s.prepare_request(requests.Request('POST', 'https://adsl.te.eg/ISP/ISP-tel.aspx',  data= data, cookies = r.cookies)))
    r = s.post('https://adsl.te.eg/ISP/ISP-tel.aspx',  data= data)
    print(r.url)