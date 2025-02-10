# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

# Print the languages and creators 
for language, creator in kata.items():
    print(f"{language} was created by {creator}")

# Expected output:
# python3 kata01.py
# Python was created by Guido van Rossum
# Ruby was created by Yukihiro Matsumoto
# PHP was created by Rasmus Lerdorf