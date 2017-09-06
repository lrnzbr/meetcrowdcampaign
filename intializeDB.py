
from model import *
import pandas as pd
import numpy as np



## Add Teams to the database


for i in range(12):
	newTeam = Team(name = "Team " + str(i+1))
	session.add(newTeam)
	session.commit()

## Add all students to the database:


students = pd.read_csv('../students.csv')

first_names = students['Student first name']
last_names = students['Student last name']
student_ids = students['ID number']
team_number = students['Team Number']

for i in range(len(first_names)):
	student = User(group = 'student', first_name = first_names[i],  last_name = last_names[i], email = first_names[i]+last_names[i][0])
	if int(team_number[i]) != 0:
		student.team_id = int(team_number[i])
	student.hash_password(str(student_ids[i])[0:9])
	session.add(student)
	session.commit()


## Add products to the database
photos = ["https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4057.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4058.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4065.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4051.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4054.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4074.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4078.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4072.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4075.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4081.JPG","https://github.com/meet-projects/KickStarter/blob/master/static/pictures/IMG_4084.JPG"]
videos = ["https://www.youtube.com/embed/RZydfIkI1f4","https://www.youtube.com/embed/Rw35xX-tAu8","https://www.youtube.com/embed/jgSUpPOf0ww","https://www.youtube.com/embed/tuh6bEbXLaM","https://www.youtube.com/embed/UJ7CnUSZvvQ","https://www.youtube.com/embed/gwMvt7RU09Q","https://www.youtube.com/embed/XmD_iChKh-g","https://www.youtube.com/embed/JtLkUoKmPZc","https://www.youtube.com/embed/D_drrBUkT88","https://www.youtube.com/embed/0Hw5i7LoPeE","https://www.youtube.com/embed/g1YGnbKKjTw"]


ipsum_he = "פנאי ניווט משחקים ארץ אל. דת ריקוד שדרות קודמות כדי, של כדי שתפו מושגי, צ'ט אל זקוק הבאים. אחרים אתנולוגיה מה עוד, אחד מה לציין בדפים. לתרום ייִדיש לאחרונה על עוד, על ויקי סרבול מתמטיקה עזה. מלא מדעי בישול איטליה ב. שמו אם לערך בויקיפדיה, זכר אל העזרה טכניים."  
ipsum_ar= "واستمر العصبة ضرب قد. وباءت الأمريكي الأوربيين هو به،, هو العالم، الثقيلة بال. مع وايرلندا الأوروبيّون كان, قد بحق أسابيع"  
ipsum_en = "Normcore banjo umami sriracha intelligentsia bushwick. Leggings kale chips iPhone prism copper mug ethical, yr fanny pack lomo live-edge tumblr selvage master cleanse pitchfork health goth. Vegan chambray listicle 90's gochujang. Seitan narwhal iceland, marfa poutine poke craft beer fixie twee PBR&B fashion axe chambray."
website_url = "http://meet.mit.edu"

for i in range(11):
	newProduct = Product(team_id = i+1, video = videos[i], photo=photos[i], description_he = ipsum_he, description_ar = ipsum_ar, description_en = ipsum_en, website_url = website_url)
	session.add(newProduct)
	session.commit()


## Add fake Users to the database

#larry = User(first_name = "Larry", last_name = "Page", username = "larry", group = 'investor bronze', email = "larry@larry.com")
#larry.hash_password("larry")
#session.add(larry)
#session.commit()

## Make a Wallet for Larry
#larrysWallet = Wallet(initial_value = '10000.00', current_value = '10000.00', user=larry)
#session.add_all([larry,larrysWallet])
#session.commit()


#jill = User(first_name = "Jill", last_name = "Scott", username = "jill", group = 'investor silver', email = "jill@jill.com")
#jill.hash_password('jill')
#session.add(jill)
#session.commit()

## Make a Wallet for  Jill
#jillsWallet = Wallet(initial_value = '50000.00', current_value = '50000.00', user = jill)
#session.add_all([jill,jillsWallet])
#session.commit()

#brad = User(first_name = "Brad", last_name = "Brown", username = "brad", group = 'investor gold', email = "brad@brad.com")
#brad.hash_password('brad')
#session.add(brad)
#session.commit()

## Make a Wallet for  Brad
#bradsWallet = Wallet(initial_value = '100000.00', current_value = '100000.00', user = brad)
#session.add_all([brad,bradsWallet])
#session.commit()



#def makeAnInvestment(user_id, product_id, amount):
#	wallet = session.query(Wallet).filter_by(user_id =user_id).one()
#	product = session.query(Product).filter_by(id = product_id).one()
#	if wallet.current_value > amount:
#		inv = Investment(wallet_id = wallet.id, product_id = product.id, amount = amount)
#		wallet.current_value = wallet.current_value - amount
#		session.add_all([wallet,inv])
#		session.commit()
#	else:
#		print("%s does not have enough money to make this investment" % wallet.user.first_name)
#Larry Invests 600 dollars in Team 4
#makeAnInvestment(71, 4, 6000.00)
#Jill Invests 4000 dollars in Team 5
#makeAnInvestment(72, 5, 4000.00)
#Brad Invests 200 dollars in Team 1
#makeAnInvestment(73, 1, 200.00)
#Brad invests 3000 dollars in Team 4
#makeAnInvestment(73,4, 3000.00)
#Print total amounts of investments for each team

#products = session.query(Product).all()
#for product in products:
#	print(product.team.name)
#	total_investments = 0.0
#	investors = []
#	for inv in product.investments:
#		total_investments += inv.amount
#		investors.append(inv.wallet.user.first_name)
#	print("Total Investments: " + str(total_investments))
#	print("Investors:")
#	print(investors)

