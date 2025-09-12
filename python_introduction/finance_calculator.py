monthly_income=int(input("Enter your monthly income:"))
total_monthly_expense=int(input("Enter your monthly expense:"))
monthly_saving=monthly_income-total_monthly_expense
rate=0.05
projected_saving=monthly_saving*12+(monthly_saving*12*0.05)
print(f"projected savings after one year, with interest, is:{projected_saving}")