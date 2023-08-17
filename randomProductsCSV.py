import csv
import random
import faker

fake = faker.Faker()

# Function to generate random color
def generate_random_color():
    colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
    return random.choice(colors)

# Function to generate random size
def generate_random_size():
    sizes = ["XS", "S", "M", "L", "XL"]
    return random.choice(sizes)

# Function to generate random price
def generate_random_price():
    return round(random.uniform(10, 1000), 2)

# Generate and populate the CSV file
with open("dummy_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "name", "color", "size", "description", "price"])

    for i in range(1000):
        id = str(i + 1) + fake.word()
        name = fake.word().capitalize()
        color = generate_random_color()
        size = generate_random_size()
        description = fake.sentence()
        price = generate_random_price()

        writer.writerow([id, name, color, size, description, price])

print("CSV file 'dummy_data.csv' created successfully.")