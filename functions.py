# Задание 8-3.
def make_skirt(size="M", text='"I love JS"' ):
    return(f"Футболка размера {size}, c надписью {text}")

print(make_skirt())
print(make_skirt("M", '"I love JS!"'))

#Задание 8-4.
def make_skirt(size="L", text='"I love Python!"' ):
    return(f"Футболка размера {size}, c надписью {text}")

print(make_skirt())
print(make_skirt("XL", '"I love JS!"'))

#Задание 8-5.
def describe_city(city_name, country_name='UK' ):
    return(f"{city_name} is in {country_name}")

print(describe_city("London"))
print(describe_city("Berlin", "Germany"))
print(describe_city("Omsk", "Russia"))