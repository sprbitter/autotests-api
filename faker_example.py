from faker import Faker

faker = Faker('ru_RU')

print(faker.name())
print(faker.first_name())
print(faker.last_name())
print(faker.address())

data = {
    "first_name": faker.first_name(),
    "last_name": faker.last_name(),
    "age": faker.random_int(18, 100),
    "email": faker.email(),
    "phone_number": faker.phone_number(),
}

print(data)