def voting_eligibility(age):
    if age > 18:
        return("eligible")
    else:
        return("not eligible")
a = voting_eligibility(23)
print(a)

