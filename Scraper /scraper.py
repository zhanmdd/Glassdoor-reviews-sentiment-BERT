import os
links = ['https://www.glassdoor.com/Overview/Working-at-HubSpot-EI_IE227605.11,18.htm',
         'https://www.glassdoor.com/Overview/Working-at-Perficient-EI_IE9329.11,21.htm',
         'https://www.glassdoor.com/Overview/Working-at-Reynolds-and-Reynolds-EI_IE564.11,32.htm',
         'https://www.glassdoor.com/Overview/Working-at-Esri-EI_IE4043.11,15.htm',
         'https://www.glassdoor.com/Overview/Working-at-Ciber-EI_IE2619.11,16.htm',
         'https://www.glassdoor.com/Overview/Working-at-Sogeti-EI_IE12028.11,17.htm',
         'https://www.glassdoor.com/Overview/Working-at-CoStar-Group-EI_IE7901.11,23.htm',
         'https://www.glassdoor.com/Overview/Working-at-MicroStrategy-EI_IE8018.11,24.htm',
         'https://www.glassdoor.com/Overview/Working-at-Payless-ShoeSource-EI_IE42821.11,29.htm',
         'https://www.glassdoor.com/Overview/Working-at-World-Wide-Technology-EI_IE9553.11,32.htm',
         'https://www.glassdoor.com/Overview/Working-at-Cadence-Design-Systems-EI_IE1217.11,33.htm',
         'https://www.glassdoor.com/Overview/Working-at-Akamai-EI_IE9219.11,17.htm',
         'https://www.glassdoor.com/Overview/Working-at-Sabre-EI_IE6269.11,16.htm',
         'https://www.glassdoor.com/Overview/Working-at-Nuance-EI_IE5667.11,17.htm',
         'https://www.glassdoor.com/Overview/Working-at-Yelp-EI_IE43314.11,15.htm',
         'https://www.glassdoor.com/Overview/Working-at-CDK-Global-EI_IE870191.11,21.htm',
         'https://www.glassdoor.com/glassdoor',
         'https://www.glassdoor.com/Overview/Working-at-Autodesk-EI_IE1155.11,19.htm',
         'https://www.glassdoor.com/Overview/Working-at-AppDynamics-EI_IE319551.11,22.htm',
         'https://www.glassdoor.com/Overview/Working-at-Zscaler-EI_IE359434.11,18.htm']

for link in links:
    glassdoor_link = 'https://www.glassdoor.com/glassdoor'
    if link !=glassdoor_link:
        company_name = link.replace('https://www.glassdoor.com/Overview/Working-at-', '')
        os.system('python main.py --headless --url "' + str(link)+ '" --limit 500 -f' + company_name +'.csv')
    else:
        os.system('python main.py --headless --url "' + str(link)+ '" --limit 500 -f glassdoor.csv')