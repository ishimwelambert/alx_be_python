monthly_income=int(input("Enter your monthly income:"))
monthly_expenses=int(input("Enter your monthly expense:"))
monthly_savings = monthly_income - monthly_expenses
rate=0.05
projected_saving=monthly_savings*12+(monthly_savings*12*0.05)
print(f"projected savings after one year, with interest, is:{projected_saving}")