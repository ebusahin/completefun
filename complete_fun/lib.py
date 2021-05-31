import random

def try_me(name):
    countries=[]
    country_list = ['Andorra', 'Albania', 'Austria', 'Belgium', 'Bulgaria', 'Belarus', 'Czech Republic', 'Germany', 'Denmark', 'Estonia', 'Finland', 'France', 'Greece', 'Hungary', 'Republic of Ireland', 'Iceland', 'Italy', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Latvia', 'Macedonia', 'Malta', 'Kingdom of the Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Sweden', 'Slovenia', 'Slovakia', 'San Marino', 'Ukraine', 'Vatican City', 'Bosnia and Herzegovina', 'Croatia', 'Moldova', 'Monaco', 'Montenegro', 'Serbia', 'Spain', 'Switzerland', 'United Kingdom', 'Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Bahrain', 'Brunei Darussalam', 'Bhutan', "People's Republic of China", 'Cyprus', 'Georgia', 'Indonesia', 'Israel', 'India', 'Iraq', 'Iran', 'Jordan', 'Japan', 'Kyrgyzstan', 'North Korea', 'South Korea', 'Kuwait', 'Lebanon', 'Myanmar', 'Mongolia', 'Maldives', 'Malaysia', 'Nepal', 'Oman', 'Philippines', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Singapore', 'Syria', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Turkey', 'Uzbekistan', 'Vietnam', 'Yemen', 'Cambodia', 'East Timor', 'Kazakhstan', 'Laos', 'Sri Lanka', 'United Arab Emirates', 'Antigua and Barbuda', 'Barbados', 'Bahamas', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Trinidad and Tobago', 'United States', 'El Salvador', 'Grenada', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Angola', 'Burkina Faso', 'Burundi', 'Benin', 'Botswana', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Ivory Coast', 'Cameroon', 'Cape Verde', 'Djibouti', 'Egypt', 'Eritrea', 'Ethiopia', 'Gabon', 'Ghana', 'The Gambia', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Liberia', 'Lesotho', 'Libya', 'Madagascar', 'Mali', 'Mauritania', 'Mauritius', 'Malawi', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Seychelles', 'Sudan', 'Sierra Leone', 'Senegal', 'Somalia', 'Sao Tome and Principe', 'Togo', 'Tunisia', 'Tanzania', 'Uganda', 'Zambia', 'Zimbabwe', 'Algeria', 'Central African Republic', 'Chad', 'Comoros', 'Equatorial Guinea', 'Morocco', 'South Africa', 'Swaziland', 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela', 'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Nauru', 'New Zealand', 'Papua New Guinea', 'Palau', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu', 'Federated States of Micronesia', 'Samoa']
    for i in country_list:
        if name[0:1] in [i[0:1] for i in country_list] or name[-3:-1] in [i[0:1] for i in country_list]:
            countries.append(i)
        elif name[0] in [i[0] for i in country_list] or name[-1] in [i[-1] for i in country_list]:
            countries.append(i)
    return countries[random.randint(0, len(countries))]


# def which_country(name, age):
#     for i in country_list:
#         if name[0:1] in [i['name'][0:1] for i in country_list]
#         and age in range(int(i(lan1)),int(i(lan2))):
#             countries.append(i)
#         else:
#             countries.append(i)
#     return [countries.random.randint(countries)]