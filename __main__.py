from models.customer import Customer

def main():
    test = Customer()
    test.set_customer_id("CUS00001")
    print("Hello World!" + test.get_customer_id())
    print(test.get_email())

if __name__ == "__main__":
    main()
