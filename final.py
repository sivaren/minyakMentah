import streamlit as st
import pandas as pd
import plotly.express as px

## MANAGING DATA
# list kode negara dari produksi_minyak_mentah.csv
kodeNegara = ['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'USA', 'OEU', 'ALB', 'DZA', 'ARG', 'ARM', 'AZE', 'BGD', 'BLR', 'BIH', 'BRA', 'BRN', 'BGR', 'KHM', 'CHL', 'CHN', 'COL', 'HRV', 'CYP', 'EGY', 'EST', 'ETH', 'GEO', 'GHA', 'HTI', 'HKG', 'IND', 'IDN', 'IRN', 'ISR', 'KAZ', 'LVA', 'LTU', 'MKD', 'MYS', 'MLT', 'MDA', 'MOZ', 'NGA', 'PAK', 'PRY', 'PER', 'PHL', 'ROU', 'RUS', 'SAU', 'SGP', 'SVN', 'ZAF', 'SDN', 'TWN', 'TZA', 'THA', 'UKR', 'ARE', 'URY', 'VNM', 'ZMB', 'WLD', 'SRB', 'MNE', 'EU28', 'G20', 'OECD', 'AGO', 'BHR', 'BEN', 'BOL', 'BWA', 'CMR', 'COG', 'CRI', 'CIV', 'CUB', 'PRK', 'COD', 'DOM', 'ECU', 'SLV', 'ERI', 'GAB', 'GTM', 'HND', 'IRQ', 'JAM', 'JOR', 'KEN', 'KWT', 'KGZ', 'LBN', 'LBY', 'MNG', 'MAR', 'MMR', 'NAM', 'NPL', 'NIC', 'NER', 'OMN', 'PAN', 'QAT', 'SEN', 'LKA', 'SYR', 'TJK', 'TGO', 'TTO', 'TUN', 'TKM', 'UZB', 'VEN', 'YEM', 'ZWE'] 
# dictCountries dari kode_negara_lengkap.json : {'Afghanistan': 'AFG', ...}
dictCountries = {'Afghanistan': 'AFG', '�land Islands': 'ALA', 'Albania': 'ALB', 'Algeria': 'DZA', 'American Samoa': 'ASM', 'Andorra': 'AND', 'Angola': 'AGO', 'Anguilla': 'AIA', 'Antarctica': 'ATA', 'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG', 'Armenia': 'ARM', 'Aruba': 'ABW', 'Australia': 'AUS', 'Austria': 'AUT', 'Azerbaijan': 'AZE', 'Bahamas': 'BHS', 'Bahrain': 'BHR', 'Bangladesh': 'BGD', 'Barbados': 'BRB', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Belize': 'BLZ', 'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN', 'Bolivia (Plurinational State of)': 'BOL', 'Bonaire, Sint Eustatius and Saba': 'BES', 'Bosnia and Herzegovina': 'BIH', 'Botswana': 'BWA', 'Bouvet Island': 'BVT', 'Brazil': 'BRA', 'British Indian Ocean Territory': 'IOT', 'Brunei Darussalam': 'BRN', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cabo Verde': 'CPV', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN', 'Cayman Islands': 'CYM', 'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 'China': 'CHN', 'Christmas Island': 'CXR', 'Cocos (Keeling) Islands': 'CCK', 'Colombia': 'COL', 'Comoros': 'COM', 'Congo': 'COG', 'Congo, Democratic Republic of the': 'COD', 'Cook Islands': 'COK', 'Costa Rica': 'CRI', "C�te d'Ivoire": 'CIV', 'Croatia': 'HRV', 'Cuba': 'CUB', 'Cura�ao': 'CUW', 'Cyprus': 'CYP', 'Czechia': 'CZE', 'Denmark': 'DNK', 'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM', 'Ecuador': 'ECU', 'Egypt': 'EGY', 'El Salvador': 'SLV', 'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Eswatini': 'SWZ', 'Ethiopia': 'ETH', 'Falkland Islands (Malvinas)': 'FLK', 'Faroe Islands': 'FRO', 'Fiji': 'FJI', 'Finland': 'FIN', 'France': 'FRA', 'French Guiana': 'GUF', 'French Polynesia': 'PYF', 'French Southern Territories': 'ATF', 'Gabon': 'GAB', 'Gambia': 'GMB', 'Georgia': 'GEO', 'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar': 'GIB', 'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD', 'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM', 'Guernsey': 'GGY', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB', 'Guyana': 'GUY', 'Haiti': 'HTI', 'Heard Island and McDonald Islands': 'HMD', 'Holy See': 'VAT', 'Honduras': 'HND', 'Hong Kong': 'HKG', 'Hungary': 'HUN', 'Iceland': 'ISL', 'India': 'IND', 'Indonesia': 'IDN', 'Iran (Islamic Republic of)': 'IRN', 'Iraq': 'IRQ', 'Ireland': 'IRL', 'Isle of Man': 'IMN', 'Israel': 'ISR', 'Italy': 'ITA', 'Jamaica': 'JAM', 'Japan': 'JPN', 'Jersey': 'JEY', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR', "Korea (Democratic People's Republic of)": 'PRK', 'Korea, Republic of': 'KOR', 'Kuwait': 'KWT', 'Kyrgyzstan': 'KGZ', "Lao People's Democratic Republic": 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'Macao': 'MAC', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT', 'Marshall Islands': 'MHL', 'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mayotte': 'MYT', 'Mexico': 'MEX', 'Micronesia (Federated States of)': 'FSM', 'Moldova, Republic of': 'MDA', 'Monaco': 'MCO', 'Mongolia': 'MNG', 'Montenegro': 'MNE', 'Montserrat': 'MSR', 'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM', 'Nauru': 'NRU', 'Nepal': 'NPL', 'Netherlands': 'NLD', 'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC', 'Niger': 'NER', 'Nigeria': 'NGA', 'Niue': 'NIU', 'Norfolk Island': 'NFK', 'North Macedonia': 'MKD', 'Northern Mariana Islands': 'MNP', 'Norway': 'NOR', 'Oman': 'OMN', 'Pakistan': 'PAK', 'Palau': 'PLW', 'Palestine, State of': 'PSE', 'Panama': 'PAN', 'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Peru': 'PER', 'Philippines': 'PHL', 'Pitcairn': 'PCN', 'Poland': 'POL', 'Portugal': 'PRT', 'Puerto Rico': 'PRI', 'Qatar': 'QAT', 'R�union': 'REU', 'Romania': 'ROU', 'Russian Federation': 'RUS', 'Rwanda': 'RWA', 'Saint Barth�lemy': 'BLM', 'Saint Helena, Ascension and Tristan da Cunha': 'SHN', 'Saint Kitts and Nevis': 'KNA', 'Saint Lucia': 'LCA', 'Saint Martin (French part)': 'MAF', 'Saint Pierre and Miquelon': 'SPM', 'Saint Vincent and the Grenadines': 'VCT', 'Samoa': 'WSM', 'San Marino': 'SMR', 'Sao Tome and Principe': 'STP', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SRB', 'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Singapore': 'SGP', 'Sint Maarten (Dutch part)': 'SXM', 'Slovakia': 'SVK', 'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM', 'South Africa': 'ZAF', 'South Georgia and the South Sandwich Islands': 'SGS', 'South Sudan': 'SSD', 'Spain': 'ESP', 'Sri Lanka': 'LKA', 'Sudan': 'SDN', 'Suriname': 'SUR', 'Svalbard and Jan Mayen': 'SJM', 'Sweden': 'SWE', 'Switzerland': 'CHE', 'Syrian Arab Republic': 'SYR', 'Taiwan, Province of China': 'TWN', 'Tajikistan': 'TJK', 'Tanzania, United Republic of': 'TZA', 'Thailand': 'THA', 'Timor-Leste': 'TLS', 'Togo': 'TGO', 'Tokelau': 'TKL', 'Tonga': 'TON', 'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Turks and Caicos Islands': 'TCA', 'Tuvalu': 'TUV', 'Uganda': 'UGA', 'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom of Great Britain and Northern Ireland': 'GBR', 'United States of America': 'USA', 'United States Minor Outlying Islands': 'UMI', 'Uruguay': 'URY', 'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 'Venezuela (Bolivarian Republic of)': 'VEN', 'Viet Nam': 'VNM', 'Virgin Islands (British)': 'VGB', 'Virgin Islands (U.S.)': 'VIR', 'Wallis and Futuna': 'WLF', 'Western Sahara': 'ESH', 'Yemen': 'YEM', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'} 
# key_list menyimpan semua key dari dictCountries: ['Afghanistan', '�land Islands', ...]
key_list = list(dictCountries.keys())
# val_list menyimpan semua value dari dictCountries: ['AFG', 'ALA', ...]
val_list = list(dictCountries.values())
# create countries name as tuple
tupCountry = ('Australia', 'Austria', 'Belgium', 'Canada', 'Czechia', 'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Korea, Republic of', 'Luxembourg', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal', 'Slovakia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'United Kingdom of Great Britain and Northern Ireland', 'United States of America', 'Albania', 'Algeria', 'Argentina', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Belarus', 'Bosnia and Herzegovina', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Cambodia', 'Chile', 'China', 'Colombia', 'Croatia', 'Cyprus', 'Egypt', 'Estonia', 'Ethiopia', 'Georgia', 'Ghana', 'Haiti', 'Hong Kong', 'India', 'Indonesia', 'Iran (Islamic Republic of)', 'Israel', 'Kazakhstan', 'Latvia', 'Lithuania', 'North Macedonia', 'Malaysia', 'Malta', 'Moldova, Republic of', 'Mozambique', 'Nigeria', 'Pakistan', 'Paraguay', 'Peru', 'Philippines', 'Romania', 'Russian Federation', 'Saudi Arabia', 'Singapore', 'Slovenia', 'South Africa', 'Sudan', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Thailand', 'Ukraine', 'United Arab Emirates', 'Uruguay', 'Viet Nam', 'Zambia', 'Serbia', 'Montenegro', 'Angola', 'Bahrain', 'Benin', 'Bolivia (Plurinational State of)', 'Botswana', 'Cameroon', 'Congo', 'Costa Rica', "C�te d'Ivoire", 'Cuba', "Korea (Democratic People's Republic of)", 'Congo, Democratic Republic of the', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Eritrea', 'Gabon', 'Guatemala', 'Honduras', 'Iraq', 'Jamaica', 'Jordan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Lebanon', 'Libya', 'Mongolia', 'Morocco', 'Myanmar', 'Namibia', 'Nepal', 'Nicaragua', 'Niger', 'Oman', 'Panama', 'Qatar', 'Senegal', 'Sri Lanka', 'Syrian Arab Republic', 'Tajikistan', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkmenistan', 'Uzbekistan', 'Venezuela (Bolivarian Republic of)', 'Yemen', 'Zimbabwe')
# regionCountries: {'AFG': 'Asia', ...}
regionCountries = {'AFG': 'Asia', 'ALA': 'Europe', 'ALB': 'Europe', 'DZA': 'Africa', 'ASM': 'Oceania', 'AND': 'Europe', 'AGO': 'Africa', 'AIA': 'Americas', 'ATA': '', 'ATG': 'Americas', 'ARG': 'Americas', 'ARM': 'Asia', 'ABW': 'Americas', 'AUS': 'Oceania', 'AUT': 'Europe', 'AZE': 'Asia', 'BHS': 'Americas', 'BHR': 'Asia', 'BGD': 'Asia', 'BRB': 'Americas', 'BLR': 'Europe', 'BEL': 'Europe', 'BLZ': 'Americas', 'BEN': 'Africa', 'BMU': 'Americas', 'BTN': 'Asia', 'BOL': 'Americas', 'BES': 'Americas', 'BIH': 'Europe', 'BWA': 'Africa', 'BVT': 'Americas', 'BRA': 'Americas', 'IOT': 'Africa', 'BRN': 'Asia', 'BGR': 'Europe', 'BFA': 'Africa', 'BDI': 'Africa', 'CPV': 'Africa', 'KHM': 'Asia', 'CMR': 'Africa', 'CAN': 'Americas', 'CYM': 'Americas', 'CAF': 'Africa', 'TCD': 'Africa', 'CHL': 'Americas', 'CHN': 'Asia', 'CXR': 'Oceania', 'CCK': 'Oceania', 'COL': 'Americas', 'COM': 'Africa', 'COG': 'Africa', 'COD': 'Africa', 'COK': 'Oceania', 'CRI': 'Americas', 'CIV': 'Africa', 'HRV': 'Europe', 'CUB': 'Americas', 'CUW': 'Americas', 'CYP': 'Asia', 'CZE': 'Europe', 'DNK': 'Europe', 'DJI': 'Africa', 'DMA': 'Americas', 'DOM': 'Americas', 'ECU': 'Americas', 'EGY': 'Africa', 'SLV': 'Americas', 'GNQ': 'Africa', 'ERI': 'Africa', 'EST': 'Europe', 'SWZ': 'Africa', 'ETH': 'Africa', 'FLK': 'Americas', 'FRO': 'Europe', 'FJI': 'Oceania', 'FIN': 'Europe', 'FRA': 'Europe', 'GUF': 'Americas', 'PYF': 'Oceania', 'ATF': 'Africa', 'GAB': 'Africa', 'GMB': 'Africa', 'GEO': 'Asia', 'DEU': 'Europe', 'GHA': 'Africa', 'GIB': 'Europe', 'GRC': 'Europe', 'GRL': 'Americas', 'GRD': 'Americas', 'GLP': 'Americas', 'GUM': 'Oceania', 'GTM': 'Americas', 'GGY': 'Europe', 'GIN': 'Africa', 'GNB': 'Africa', 'GUY': 'Americas', 'HTI': 'Americas', 'HMD': 'Oceania', 'VAT': 'Europe', 'HND': 'Americas', 'HKG': 'Asia', 'HUN': 'Europe', 'ISL': 'Europe', 'IND': 'Asia', 'IDN': 'Asia', 'IRN': 'Asia', 'IRQ': 'Asia', 'IRL': 'Europe', 'IMN': 'Europe', 'ISR': 'Asia', 'ITA': 'Europe', 'JAM': 'Americas', 'JPN': 'Asia', 'JEY': 'Europe', 'JOR': 'Asia', 'KAZ': 'Asia', 'KEN': 'Africa', 'KIR': 'Oceania', 'PRK': 'Asia', 'KOR': 'Asia', 'KWT': 'Asia', 'KGZ': 'Asia', 'LAO': 'Asia', 'LVA': 'Europe', 'LBN': 'Asia', 'LSO': 'Africa', 'LBR': 'Africa', 'LBY': 'Africa', 'LIE': 'Europe', 'LTU': 'Europe', 'LUX': 'Europe', 'MAC': 'Asia', 'MDG': 'Africa', 'MWI': 'Africa', 'MYS': 'Asia', 'MDV': 'Asia', 'MLI': 'Africa', 'MLT': 'Europe', 'MHL': 'Oceania', 'MTQ': 'Americas', 'MRT': 'Africa', 'MUS': 'Africa', 'MYT': 'Africa', 'MEX': 'Americas', 'FSM': 'Oceania', 'MDA': 'Europe', 'MCO': 'Europe', 'MNG': 'Asia', 'MNE': 'Europe', 'MSR': 'Americas', 'MAR': 'Africa', 'MOZ': 'Africa', 'MMR': 'Asia', 'NAM': 'Africa', 'NRU': 'Oceania', 'NPL': 'Asia', 'NLD': 'Europe', 'NCL': 'Oceania', 'NZL': 'Oceania', 'NIC': 'Americas', 'NER': 'Africa', 'NGA': 'Africa', 'NIU': 'Oceania', 'NFK': 'Oceania', 'MKD': 'Europe', 'MNP': 'Oceania', 'NOR': 'Europe', 'OMN': 'Asia', 'PAK': 'Asia', 'PLW': 'Oceania', 'PSE': 'Asia', 'PAN': 'Americas', 'PNG': 'Oceania', 'PRY': 'Americas', 'PER': 'Americas', 'PHL': 'Asia', 'PCN': 'Oceania', 'POL': 'Europe', 'PRT': 'Europe', 'PRI': 'Americas', 'QAT': 'Asia', 'REU': 'Africa', 'ROU': 'Europe', 'RUS': 'Europe', 'RWA': 'Africa', 'BLM': 'Americas', 'SHN': 'Africa', 'KNA': 'Americas', 'LCA': 'Americas', 'MAF': 'Americas', 'SPM': 'Americas', 'VCT': 'Americas', 'WSM': 'Oceania', 'SMR': 'Europe', 'STP': 'Africa', 'SAU': 'Asia', 'SEN': 'Africa', 'SRB': 'Europe', 'SYC': 'Africa', 'SLE': 'Africa', 'SGP': 'Asia', 'SXM': 'Americas', 'SVK': 'Europe', 'SVN': 'Europe', 'SLB': 'Oceania', 'SOM': 'Africa', 'ZAF': 'Africa', 'SGS': 'Americas', 'SSD': 'Africa', 'ESP': 'Europe', 'LKA': 'Asia', 'SDN': 'Africa', 'SUR': 'Americas', 'SJM': 'Europe', 'SWE': 'Europe', 'CHE': 'Europe', 'SYR': 'Asia', 'TWN': 'Asia', 'TJK': 'Asia', 'TZA': 'Africa', 'THA': 'Asia', 'TLS': 'Asia', 'TGO': 'Africa', 'TKL': 'Oceania', 'TON': 'Oceania', 'TTO': 'Americas', 'TUN': 'Africa', 'TUR': 'Asia', 'TKM': 'Asia', 'TCA': 'Americas', 'TUV': 'Oceania', 'UGA': 'Africa', 'UKR': 'Europe', 'ARE': 'Asia', 'GBR': 'Europe', 'USA': 'Americas', 'UMI': 'Oceania', 'URY': 'Americas', 'UZB': 'Asia', 'VUT': 'Oceania', 'VEN': 'Americas', 'VNM': 'Asia', 'VGB': 'Americas', 'VIR': 'Americas', 'WLF': 'Oceania', 'ESH': 'Africa', 'YEM': 'Asia', 'ZMB': 'Africa', 'ZWE': 'Africa'} 
# subRegionCountries: {'AFG': 'Southern Asia', ...}
subRegionCountries = {'AFG': 'Southern Asia', 'ALA': 'Northern Europe', 'ALB': 'Southern Europe', 'DZA': 'Northern Africa', 'ASM': 'Polynesia', 'AND': 'Southern Europe', 'AGO': 'Sub-Saharan Africa', 'AIA': 'Latin America and the Caribbean', 'ATA': '', 'ATG': 'Latin America and the Caribbean', 'ARG': 'Latin America and the Caribbean', 'ARM': 'Western Asia', 'ABW': 'Latin America and the Caribbean', 'AUS': 'Australia and New Zealand', 'AUT': 'Western Europe', 'AZE': 'Western Asia', 'BHS': 'Latin America and the Caribbean', 'BHR': 'Western Asia', 'BGD': 'Southern Asia', 'BRB': 'Latin America and the Caribbean', 'BLR': 'Eastern Europe', 'BEL': 'Western Europe', 'BLZ': 'Latin America and the Caribbean', 'BEN': 'Sub-Saharan Africa', 'BMU': 'Northern America', 'BTN': 'Southern Asia', 'BOL': 'Latin America and the Caribbean', 'BES': 'Latin America and the Caribbean', 'BIH': 'Southern Europe', 'BWA': 'Sub-Saharan Africa', 'BVT': 'Latin America and the Caribbean', 'BRA': 'Latin America and the Caribbean', 'IOT': 'Sub-Saharan Africa', 'BRN': 'South-eastern Asia', 'BGR': 'Eastern Europe', 'BFA': 'Sub-Saharan Africa', 'BDI': 'Sub-Saharan Africa', 'CPV': 'Sub-Saharan Africa', 'KHM': 'South-eastern Asia', 'CMR': 'Sub-Saharan Africa', 'CAN': 'Northern America', 'CYM': 'Latin America and the Caribbean', 'CAF': 'Sub-Saharan Africa', 'TCD': 'Sub-Saharan Africa', 'CHL': 'Latin America and the Caribbean', 'CHN': 'Eastern Asia', 'CXR': 'Australia and New Zealand', 'CCK': 'Australia and New Zealand', 'COL': 'Latin America and the Caribbean', 'COM': 'Sub-Saharan Africa', 'COG': 'Sub-Saharan Africa', 'COD': 'Sub-Saharan Africa', 'COK': 'Polynesia', 'CRI': 'Latin America and the Caribbean', 'CIV': 'Sub-Saharan Africa', 'HRV': 'Southern Europe', 'CUB': 'Latin America and the Caribbean', 'CUW': 'Latin America and the Caribbean', 'CYP': 'Western Asia', 'CZE': 'Eastern Europe', 'DNK': 'Northern Europe', 'DJI': 'Sub-Saharan Africa', 'DMA': 'Latin America and the Caribbean', 'DOM': 'Latin America and the Caribbean', 'ECU': 'Latin America and the Caribbean', 'EGY': 'Northern Africa', 'SLV': 'Latin America and the Caribbean', 'GNQ': 'Sub-Saharan Africa', 'ERI': 'Sub-Saharan Africa', 'EST': 'Northern Europe', 'SWZ': 'Sub-Saharan Africa', 'ETH': 'Sub-Saharan Africa', 'FLK': 'Latin America and the Caribbean', 'FRO': 'Northern Europe', 'FJI': 'Melanesia', 'FIN': 'Northern Europe', 'FRA': 'Western Europe', 'GUF': 'Latin America and the Caribbean', 'PYF': 'Polynesia', 'ATF': 'Sub-Saharan Africa', 'GAB': 'Sub-Saharan Africa', 'GMB': 'Sub-Saharan Africa', 'GEO': 'Western Asia', 'DEU': 'Western Europe', 'GHA': 'Sub-Saharan Africa', 'GIB': 'Southern Europe', 'GRC': 'Southern Europe', 'GRL': 'Northern America', 'GRD': 'Latin America and the Caribbean', 'GLP': 'Latin America and the Caribbean', 'GUM': 'Micronesia', 'GTM': 'Latin America and the Caribbean', 'GGY': 'Northern Europe', 'GIN': 'Sub-Saharan Africa', 'GNB': 'Sub-Saharan Africa', 'GUY': 'Latin America and the Caribbean', 'HTI': 'Latin America and the Caribbean', 'HMD': 'Australia and New Zealand', 'VAT': 'Southern Europe', 'HND': 'Latin America and the Caribbean', 'HKG': 'Eastern Asia', 'HUN': 'Eastern Europe', 'ISL': 'Northern Europe', 'IND': 'Southern Asia', 'IDN': 'South-eastern Asia', 'IRN': 'Southern Asia', 'IRQ': 'Western Asia', 'IRL': 'Northern Europe', 'IMN': 'Northern Europe', 'ISR': 'Western Asia', 'ITA': 'Southern Europe', 'JAM': 'Latin America and the Caribbean', 'JPN': 'Eastern Asia', 'JEY': 'Northern Europe', 'JOR': 'Western Asia', 'KAZ': 'Central Asia', 'KEN': 'Sub-Saharan Africa', 'KIR': 'Micronesia', 'PRK': 'Eastern Asia', 'KOR': 'Eastern Asia', 'KWT': 'Western Asia', 'KGZ': 'Central Asia', 'LAO': 'South-eastern Asia', 'LVA': 'Northern Europe', 'LBN': 'Western Asia', 'LSO': 'Sub-Saharan Africa', 'LBR': 'Sub-Saharan Africa', 'LBY': 'Northern Africa', 'LIE': 'Western Europe', 'LTU': 'Northern Europe', 'LUX': 'Western Europe', 'MAC': 'Eastern Asia', 'MDG': 'Sub-Saharan Africa', 'MWI': 'Sub-Saharan Africa', 'MYS': 'South-eastern Asia', 'MDV': 'Southern Asia', 'MLI': 'Sub-Saharan Africa', 'MLT': 'Southern Europe', 'MHL': 'Micronesia', 'MTQ': 'Latin America and the Caribbean', 'MRT': 'Sub-Saharan Africa', 'MUS': 'Sub-Saharan Africa', 'MYT': 'Sub-Saharan Africa', 'MEX': 'Latin America and the Caribbean', 'FSM': 'Micronesia', 'MDA': 'Eastern Europe', 'MCO': 'Western Europe', 'MNG': 'Eastern Asia', 'MNE': 'Southern Europe', 'MSR': 'Latin America and the Caribbean', 'MAR': 'Northern Africa', 'MOZ': 'Sub-Saharan Africa', 'MMR': 'South-eastern Asia', 'NAM': 'Sub-Saharan Africa', 'NRU': 'Micronesia', 'NPL': 'Southern Asia', 'NLD': 'Western Europe', 'NCL': 'Melanesia', 'NZL': 'Australia and New Zealand', 'NIC': 'Latin America and the Caribbean', 'NER': 'Sub-Saharan Africa', 'NGA': 'Sub-Saharan Africa', 'NIU': 'Polynesia', 'NFK': 'Australia and New Zealand', 'MKD': 'Southern Europe', 'MNP': 'Micronesia', 'NOR': 'Northern Europe', 'OMN': 'Western Asia', 'PAK': 'Southern Asia', 'PLW': 'Micronesia', 'PSE': 'Western Asia', 'PAN': 'Latin America and the Caribbean', 'PNG': 'Melanesia', 'PRY': 'Latin America and the Caribbean', 'PER': 'Latin America and the Caribbean', 'PHL': 'South-eastern Asia', 'PCN': 'Polynesia', 'POL': 'Eastern Europe', 'PRT': 'Southern Europe', 'PRI': 'Latin America and the Caribbean', 'QAT': 'Western Asia', 'REU': 'Sub-Saharan Africa', 'ROU': 'Eastern Europe', 'RUS': 'Eastern Europe', 'RWA': 'Sub-Saharan Africa', 'BLM': 'Latin America and the Caribbean', 'SHN': 'Sub-Saharan Africa', 'KNA': 'Latin America and the Caribbean', 'LCA': 'Latin America and the Caribbean', 'MAF': 'Latin America and the Caribbean', 'SPM': 'Northern America', 'VCT': 'Latin America and the Caribbean', 'WSM': 'Polynesia', 'SMR': 'Southern Europe', 'STP': 'Sub-Saharan Africa', 'SAU': 'Western Asia', 'SEN': 'Sub-Saharan Africa', 'SRB': 'Southern Europe', 'SYC': 'Sub-Saharan Africa', 'SLE': 'Sub-Saharan Africa', 'SGP': 'South-eastern Asia', 'SXM': 'Latin America and the Caribbean', 'SVK': 'Eastern Europe', 'SVN': 'Southern Europe', 'SLB': 'Melanesia', 'SOM': 'Sub-Saharan Africa', 'ZAF': 'Sub-Saharan Africa', 'SGS': 'Latin America and the Caribbean', 'SSD': 'Sub-Saharan Africa', 'ESP': 'Southern Europe', 'LKA': 'Southern Asia', 'SDN': 'Northern Africa', 'SUR': 'Latin America and the Caribbean', 'SJM': 'Northern Europe', 'SWE': 'Northern Europe', 'CHE': 'Western Europe', 'SYR': 'Western Asia', 'TWN': 'Eastern Asia', 'TJK': 'Central Asia', 'TZA': 'Sub-Saharan Africa', 'THA': 'South-eastern Asia', 'TLS': 'South-eastern Asia', 'TGO': 'Sub-Saharan Africa', 'TKL': 'Polynesia', 'TON': 'Polynesia', 'TTO': 'Latin America and the Caribbean', 'TUN': 'Northern Africa', 'TUR': 'Western Asia', 'TKM': 'Central Asia', 'TCA': 'Latin America and the Caribbean', 'TUV': 'Polynesia', 'UGA': 'Sub-Saharan Africa', 'UKR': 'Eastern Europe', 'ARE': 'Western Asia', 'GBR': 'Northern Europe', 'USA': 'Northern America', 'UMI': 'Micronesia', 'URY': 'Latin America and the Caribbean', 'UZB': 'Central Asia', 'VUT': 'Melanesia', 'VEN': 'Latin America and the Caribbean', 'VNM': 'South-eastern Asia', 'VGB': 'Latin America and the Caribbean', 'VIR': 'Latin America and the Caribbean', 'WLF': 'Polynesia', 'ESH': 'Northern Africa', 'YEM': 'Western Asia', 'ZMB': 'Sub-Saharan Africa', 'ZWE': 'Sub-Saharan Africa'}
# some organization (not country)
someOrg = ['OEU', 'WLD', 'EU28', 'G20', 'OECD']

# INISIALISASI DATA
rawData = pd.read_csv("produksi_minyak_mentah.csv")
# ASSIGN KOLOM produksi_kumulatif = 0
rawData = rawData.assign(produksi_kumulatif = 0)
# UPDATE VALUE DARI KOLOM produksi_kumulatif
rawData["produksi_kumulatif"] = rawData.groupby(["kode_negara"])["produksi"].cumsum()
# ASSIGN DATA FINAL
data = rawData

# data yang berisi organisasi dunia (tanpa country)
dataOrg = data.loc[(data["kode_negara"] == 'OEU') | (data["kode_negara"] == 'WLD') | (data["kode_negara"] == 'EU28') | (data["kode_negara"] == 'G20') | (data["kode_negara"] == 'OECD')]
dataOrgAsc = dataOrg.sort_values(["produksi"], ascending=[1])
dataOrgDsc = dataOrg.sort_values(["produksi"], ascending=[0])

## FUNCTIONS
# FUNGSI UNTUK SOAL A
def get_CountryProduction_byYear(countryName, data):
    # mengambil dictCountries dari global, agar dapat di akses dalam fungsi
    global dictCountries

    alpha3 = dictCountries[countryName]
    df = data.loc[(data["kode_negara"] == alpha3)]
    
    return df
# FUNGSI UNTUK SOAL B
def get_CountriesProduction_aYear(B,T,data):
    df1 = data[["kode_negara", "tahun", "produksi"]]
    df2 = df1.loc[(data["tahun"] == T)]
    df3 = df2.loc[(data["kode_negara"] != 'OEU') & (data["kode_negara"] != 'WLD') & (data["kode_negara"] != 'EU28') & (data["kode_negara"] != 'G20') & (data["kode_negara"] != 'OECD')]
    df4 = df3.sort_values(["produksi"], ascending=[0])
    df5 = df4[:B]
    
    return df5
# FUNGSI UNTUK SOAL C
def get_countries_cumProduction(B, data):
    df1 = data.loc[(data["kode_negara"] != 'OEU') & (data["kode_negara"] != 'WLD') & (data["kode_negara"] != 'EU28') & (data["kode_negara"] != 'G20') & (data["kode_negara"] != 'OECD')]
    df2 = df1.groupby("kode_negara")["tahun","produksi_kumulatif"].max().reset_index()
    df3 = df2.sort_values(["produksi_kumulatif"], ascending=[0])
    df4 = df3[:B]
    
    return df4
# FUNGSI UNTUK SOAL D
def get_extremeData_byYear(T,data):
    # data hanya untuk negara (tanpa organisasi)
    dfCountry = data.loc[(data["kode_negara"] != 'OEU') & (data["kode_negara"] != 'WLD') & (data["kode_negara"] != 'EU28') & (data["kode_negara"] != 'G20') & (data["kode_negara"] != 'OECD')]
    # data untuk tahun T
    dfT = dfCountry.loc[(dfCountry["tahun"] == T)]
    # data dengan produksi != 0 pada tahun T
    dfTAvail = dfT.loc[(dfT["produksi"] != 0)]
    # data dengan produksi != 0
    dfAvail = dfCountry.loc[(dfCountry["produksi"] != 0)]

    dfMaxT = dfT.sort_values(["produksi"], ascending=[0])
    dfMaxT = dfMaxT[:1]
    dfMax = dfCountry.sort_values(["produksi"], ascending=[0])
    dfMax = dfMax[:1]

    dfMinT = dfTAvail.sort_values(["produksi"], ascending=[1])
    dfMinT = dfMinT[:1]
    dfMin = dfAvail.sort_values(["produksi"], ascending=[1])
    dfMin = dfMin[:1]

    dfNullT = dfT.loc[(dfT["produksi"] == 0)]
    dfNullT = dfNullT[:1]
    dfNull = dfCountry.loc[(dfCountry["produksi"] == 0)]
    dfNull = dfNull[:1]

    return dfMaxT, dfMax, dfMinT, dfMin, dfNullT, dfNull

## STREAMLIT INTERACTIVE
# HEADER
st.markdown(f"<h1 style='text-align: center'>Informasi Seputar Data Produksi Minyak Mentah dari Berbagai Negara di Seluruh Dunia</h1>", unsafe_allow_html=True)
st.markdown('''---''')
# ABOUT PROGRAM
st.info('''##### ABOUT THIS PROGRAM:
''')
st.info('''
###### MENU 1
Grafik jumlah produksi minyak mentah terhadap waktu (tahun) dari suatu negara N, dimana nilai
N dapat dipilih oleh user secara interaktif. Nama negara N dituliskan secara lengkap bukan kode
negaranya.\n
**_default value (N): Australia_**

---
###### MENU 2
Grafik yang menunjukan B-besar negara dengan jumlah produksi terbesar pada tahun T, dimana
nilai B dan T dapat dipilih oleh user secara interaktif.\n
**_default value (B,T): 5, 2000_**

---
###### MENU 3
Grafik yang menunjukan B-besar negara dengan jumlah produksi terbesar secara kumulatif
keseluruhan tahun, dimana nilai B dapat dipilih oleh user secara interaktif.\n
**_default value (B): 4_**

---
###### MENU 4
Informasi yang menyebutkan: (1) nama lengkap negara, kode negara, region, dan sub-region
dengan jumlah produksi terbesar pada tahun T dan keseluruhan tahun. (1) nama lengkap negara,
kode negara, region, dan sub-region dengan jumlah produksi terkecil (tidak sama dengan nol)
pada tahun T dan keseluruhan tahun. (1) nama lengkap negara, kode negara, region, dan
sub-region dengan jumlah produksi sama dengan nol pada tahun T dan keseluruhan tahun.\n
**_default value (T): 2010_**

---
###### FUN FACT!
Informasi yang menunjukkan jumlah terkecil dan terbesar produksi minyak mentah (_beserta tahunnya_) dari organisasi-organisasi yang ada di dunia.\n

''')
st.write('''---''')

## MENUS
#  MENU 1
with st.container():
    st.markdown("## MENU 1")
    countryInput_menu1 = st.selectbox('Pilih Negara:', tupCountry)

    with st.container():
        st.markdown("<hr>", unsafe_allow_html=True)
        col1_menu1, col2_menu1 = st.columns([2,4])

        dfMenu1Raw = get_CountryProduction_byYear(countryInput_menu1,data)
        dfMenu1 = dfMenu1Raw.set_index("tahun")[["produksi"]]
        
        col1_menu1.write(dfMenu1)
        col2_menu1.write(f"> ### Tabel disamping adalah jumlah produksi minyak mentah Negara {countryInput_menu1} per tahun!")

    fig1 = px.line(dfMenu1, labels={'value': 'JUMLAH PRODUKSI', 'tahun':'TAHUN'})
    fig1.update_layout(
        margin=dict(
            t=5,
            b=1
        )
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center'>Line Chart <br> </h4>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center'>Jumlah Produksi Minyak Negara {countryInput_menu1} terhadap Waktu (tahun)</h5>", unsafe_allow_html=True)
    st.write(fig1)
    st.markdown("<hr>", unsafe_allow_html=True)

#  MENU 2
with st.container():
    st.markdown("## MENU 2")
    st.warning("###### _Atur besar interval yang diinginkan!_")
    intervalInput_menu2 = st.slider('Interval', min_value=1, max_value=142, value=5, step=1)
    tahunInput_menu2 = st.number_input("Masukkan tahun (1971-2015):", min_value=1971, max_value=2015, value=2000)
    st.markdown("<hr>", unsafe_allow_html=True)

    with st.container():
        col1_menu2, col2_menu2 = st.columns([4,3])
        
        dfMenu2Raw = get_CountriesProduction_aYear(intervalInput_menu2,tahunInput_menu2,data)
        dfMenu2_show = dfMenu2Raw.set_index("kode_negara")[["tahun","produksi"]]
        dfMenu2 = dfMenu2Raw[["kode_negara","produksi"]]
        
        col1_menu2.markdown(f"> ### Berikut adalah {intervalInput_menu2} besar negara dengan jumlah produksi terbesar pada tahun {'%.0f' % tahunInput_menu2}!")
        col2_menu2.write(dfMenu2_show)

    fig2 = px.bar(dfMenu2, x="kode_negara", y="produksi", labels={'kode_negara':'KODE NEGARA', 'produksi':'JUMLAH PRODUKSI'}, color="kode_negara")
    fig2.update_layout(
        margin=dict(
            t=5,
            b=1
        )
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center'>Bar Chart <br> </h4>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center'>{intervalInput_menu2} Negara dengan Jumlah Produksi Minyak Terbesar pada Tahun {'%.0f' % tahunInput_menu2}</h5>", unsafe_allow_html=True)
    st.write(fig2)
    st.markdown("<hr>", unsafe_allow_html=True)

#  MENU 3
with st.container():
    st.markdown("## MENU 3")
    st.warning("###### _Atur besar interval yang diinginkan!_")
    intervalInput_menu3 = st.slider('Interval', min_value=1, max_value=142, value=4, step=1)

    with st.container():
        st.markdown("<hr>", unsafe_allow_html=True)
        col1_menu3, col2_menu3 = st.columns([3,5])

        dfMenu3Raw = get_countries_cumProduction(intervalInput_menu3, data)
        dfMenu3_show = dfMenu3Raw.set_index("kode_negara")[["produksi_kumulatif"]]
        dfMenu3 = dfMenu3Raw[["kode_negara","produksi_kumulatif"]]

        col1_menu3.write(dfMenu3_show)
        col2_menu3.markdown(f"> #### Tabel disamping menampilkan {intervalInput_menu3} besar negara dengan jumlah produksi kumulatif terbesar sepanjang tahun!")

    fig3 = px.bar(dfMenu3, x="kode_negara", y="produksi_kumulatif", labels={'kode_negara':'KODE NEGARA', 'produksi_kumulatif':'JUMLAH PRODUKSI KUMULATIF'}, color="produksi_kumulatif")
    fig3.update_layout(
        margin=dict(
            t=5,
            b=1
        )
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center'>Bar Chart <br> </h4>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center'>{intervalInput_menu3} Negara dengan Jumlah Produksi Minyak Kumulatif Terbesar Sepanjang Tahun</h5>", unsafe_allow_html=True)
    st.write(fig3)
    st.markdown("<hr>", unsafe_allow_html=True)

#  MENU 4
with st.container():
    st.markdown("## MENU 4")
    tahunInput_menu4 = st.number_input("Masukkan tahun (1971-2015):", min_value=1971, max_value=2015, value=2010)
    st.markdown("<hr>", unsafe_allow_html=True)

    dfMenu4_1, dfMenu4_2, dfMenu4_3, dfMenu4_4, dfMenu4_5, dfMenu4_6 = get_extremeData_byYear(tahunInput_menu4,data)
    dfMenu4_1_show = dfMenu4_1.set_index("kode_negara")[["tahun","produksi"]]
    dfMenu4_2_show = dfMenu4_2.set_index("kode_negara")[["tahun","produksi"]]
    dfMenu4_3_show = dfMenu4_3.set_index("kode_negara")[["tahun","produksi"]]
    dfMenu4_4_show = dfMenu4_4.set_index("kode_negara")[["tahun","produksi"]]
    dfMenu4_5_show = dfMenu4_5.set_index("kode_negara")[["tahun","produksi"]]
    dfMenu4_6_show = dfMenu4_6.set_index("kode_negara")[["tahun","produksi"]]

    # MENU 4.1
    c1_menu4, c2_menu4 = st.columns([5,3])
    kode_negara1 = dfMenu4_1.iloc[0]["kode_negara"]
    negara1 = key_list[val_list.index(kode_negara1)]
    reg_negara1 = regionCountries[kode_negara1]
    subReg_negara1 = subRegionCountries[kode_negara1]
    c1_menu4.info(f'''
    ##### Data dengan jumlah produksi terbesar pada tahun {'%.0f' % tahunInput_menu4}
    ''')
    c1_menu4.info(f'''
    ###### NAMA NEGARA : {negara1}\n
    ###### KODE NEGARA : {kode_negara1}\n
    ###### REGION      : {reg_negara1}\n
    ###### SUB-REGION  : {subReg_negara1}
    ''')
    c2_menu4.write(dfMenu4_1_show)
    st.markdown("<hr>", unsafe_allow_html=True)

    # MENU 4.2
    c3_menu4, c4_menu4 = st.columns([3,5])
    kode_negara2 = dfMenu4_2.iloc[0]["kode_negara"]
    negara2 = key_list[val_list.index(kode_negara2)]
    reg_negara2 = regionCountries[kode_negara2]
    subReg_negara2 = subRegionCountries[kode_negara2]
    c4_menu4.info(f'''
    ##### Data dengan jumlah produksi terbesar sepanjang tahun
    ''')
    c4_menu4.info(f'''
    ###### NAMA NEGARA : {negara2}\n
    ###### KODE NEGARA : {kode_negara2}\n
    ###### REGION      : {reg_negara2}\n
    ###### SUB-REGION  : {subReg_negara2}
    ''')
    c3_menu4.write(dfMenu4_2_show) 
    st.markdown("<hr>", unsafe_allow_html=True)

    # MENU 4.3
    c5_menu4, c6_menu4 = st.columns([5,3])
    kode_negara3 = dfMenu4_3.iloc[0]["kode_negara"]
    negara3 = key_list[val_list.index(kode_negara3)]
    reg_negara3 = regionCountries[kode_negara3]
    subReg_negara3 = subRegionCountries[kode_negara3]
    c5_menu4.info(f'''
    ##### Data dengan jumlah produksi terkecil pada tahun {'%.0f' % tahunInput_menu4}
    ''')
    c5_menu4.info(f'''
    ###### NAMA NEGARA : {negara3}\n
    ###### KODE NEGARA : {kode_negara3}\n
    ###### REGION      : {reg_negara3}\n
    ###### SUB-REGION  : {subReg_negara3}
    ''')
    c6_menu4.write(dfMenu4_3_show)
    st.markdown("<hr>", unsafe_allow_html=True)

    # MENU 4.4
    c7_menu4, c8_menu4 = st.columns([3,5])
    kode_negara4 = dfMenu4_4.iloc[0]["kode_negara"]
    negara4 = key_list[val_list.index(kode_negara4)]
    reg_negara4 = regionCountries[kode_negara4]
    subReg_negara4 = subRegionCountries[kode_negara4]
    c8_menu4.info(f'''
    ##### Data dengan jumlah produksi terkecil sepanjang tahun
    ''')
    c8_menu4.info(f'''
    ###### NAMA NEGARA : {negara4}\n
    ###### KODE NEGARA : {kode_negara4}\n
    ###### REGION      : {reg_negara4}\n
    ###### SUB-REGION  : {subReg_negara4}
    ''')
    c7_menu4.write(dfMenu4_4_show)
    st.markdown("<hr>", unsafe_allow_html=True)

    # MENU 4.5
    c9_menu4, c10_menu4 = st.columns([5,3])
    kode_negara5 = dfMenu4_5.iloc[0]["kode_negara"]
    negara5 = key_list[val_list.index(kode_negara5)]
    reg_negara5 = regionCountries[kode_negara5]
    subReg_negara5 = subRegionCountries[kode_negara5]
    c9_menu4.info(f'''
    ##### Data dengan jumlah produksi sama dengan nol pada tahun {'%.0f' % tahunInput_menu4}
    ''')
    c9_menu4.info(f'''
    ###### NAMA NEGARA : {negara5}\n
    ###### KODE NEGARA : {kode_negara5}\n
    ###### REGION      : {reg_negara5}\n
    ###### SUB-REGION  : {subReg_negara5}
    ''')
    c10_menu4.write(dfMenu4_5_show)
    st.markdown("<hr>", unsafe_allow_html=True)

    # MENU 4.6
    c11_menu4, c12_menu4 = st.columns([3,5])
    kode_negara6 = dfMenu4_6.iloc[0]["kode_negara"]
    negara6 = key_list[val_list.index(kode_negara6)]
    reg_negara6 = regionCountries[kode_negara6]
    subReg_negara6 = subRegionCountries[kode_negara6]
    c12_menu4.info(f'''
    ##### Data dengan jumlah produksi sama dengan nol sepanjang tahun
    ''')
    c12_menu4.info(f'''
    ###### NAMA NEGARA : {negara6}\n
    ###### KODE NEGARA : {kode_negara6}\n
    ###### REGION      : {reg_negara6}\n
    ###### SUB-REGION  : {subReg_negara6}
    ''')
    c11_menu4.write(dfMenu4_6_show)
    st.markdown("<hr>", unsafe_allow_html=True)

# FUN FACT!
st.success('''
## FUN FACT!
''')
st.success(f'''
##### OEU Organization (OEU)
Data dengan jumlah produksi terkecil terjadi pada tahun **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='OEU'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='OEU'].iloc[0]["produksi"]}**.\n
Data dengan jumlah produksi terbesar terjadi pada tahun **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='OEU'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='OEU'].iloc[0]["produksi"]}**.

---
##### Organisation for Economic Co-operation and Development (OECD)
Data dengan jumlah produksi terkecil terjadi pada tahun **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='OECD'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='OECD'].iloc[0]["produksi"]}**.\n
Data dengan jumlah produksi terbesar terjadi pada tahun **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='OECD'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='OECD'].iloc[0]["produksi"]}**.

---
##### The Group of Twenty (G20)
Data dengan jumlah produksi terkecil terjadi pada tahun **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='G20'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='G20'].iloc[0]["produksi"]}**.\n
Data dengan jumlah produksi terbesar terjadi pada tahun **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='G20'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='G20'].iloc[0]["produksi"]}**.

---
##### Twenty Eight Member States of The European Union (EU28)
Data dengan jumlah produksi terkecil terjadi pada tahun **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='EU28'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='EU28'].iloc[0]["produksi"]}**.\n
Data dengan jumlah produksi terbesar terjadi pada tahun **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='EU28'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='EU28'].iloc[0]["produksi"]}**.

---
##### The World (WLD)
Data dengan jumlah produksi terkecil terjadi pada tahun **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='WLD'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgAsc.loc[dataOrgAsc["kode_negara"]=='WLD'].iloc[0]["produksi"]}**.\n
Data dengan jumlah produksi terbesar terjadi pada tahun **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='WLD'].iloc[0]["tahun"]}** yaitu sebesar **{dataOrgDsc.loc[dataOrgDsc["kode_negara"]=='WLD'].iloc[0]["produksi"]}**.

''')

# FOOTER
st.markdown('''---''')
st.markdown(f"<h1 style='text-align: center'>TERIMA KASIH, SAMPAI JUMPA! <br> </h1>", unsafe_allow_html=True)
