replaced ethnic group strings by numeric values like this:

    data['race'] = data['race'].replace(to_replace="White", value=0)
    data['race'] = data['race'].replace(to_replace="Amerindian", value=1)
    data['race'] = data['race'].replace(to_replace="Asian", value=2)
    data['race'] = data['race'].replace(to_replace="Black", value=3)
    data['race'] = data['race'].replace(to_replace="Hispanic", value=4)
    data['race'] = data['race'].replace(to_replace="Mexican", value=5)
    data['race'] = data['race'].replace(to_replace="Other", value=6)
    data['race'] = data['race'].replace(to_replace="Puertorican", value=7)
