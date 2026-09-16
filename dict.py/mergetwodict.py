cities ={"bhimaram": "63736","hyberabad":"7282j"}
cities_india = {"bangealore":"781f","Mumbai":"623ts7"}
cities.update(cities_india)

print(cities)


#merge(|)
cities ={"bhimaram": "63736","hyberabad":"7282j"}
cities_india = {"bangealore":"781f","Mumbai":"623ts7"}

r =  cities| cities_india

print(r)

#Using unpacking operator (**):

cities ={"bhimaram": "63736","hyberabad":"7282j"}
cities_india = {"bangealore":"781f","Mumbai":"623ts7"}

r ={**cities,**cities_india}

print(r)
