class Pakistan:
    def capital(self):
        print("The capital of pakistan in Islamabad")

    def language(self):
        print("The official language of pakistan is Urdu")

    def type_of_country(self):
        print("Pakistan is an authorotarian country")
    

class India:
    def capital(self):
        print("Capital of India is New Delhi.")

    def language(self):
        print("The language of india in hindi.")

    def type_of_country(self):
        print("India is a democratic country.")


def get_info_about_country(country: Pakistan | India):
    country.capital()
    country.language()
    country.type_of_country()


pakistan = Pakistan()
india = India()


get_info_about_country(pakistan)
get_info_about_country(india)