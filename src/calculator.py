# src/calculator.py

def calculate_bmr(weight_kg, height_cm, age, gender):
    """
    Mifflin-St Jeor Equation
    gender: 'M' or 'F'
    """
    base = 10 * weight_kg + 6.25 * height_cm - 5 * age
    if gender == 'M':
        return base + 5
    else:
        return base - 161

def calculate_tdee(bmr, activity_level):
    """
    activity_level:
    1.2  = 久坐
    1.375 = 輕度運動（每週1-3天）
    1.55  = 中度運動（每週3-5天）
    1.725 = 高度運動（每週6-7天）
    1.9   = 運動員
    """
    return bmr * activity_level

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    else:
        return "肥胖"
    
if __name__ == "__main__":
    bmr = calculate_bmr(70, 175, 25, 'M')
    tdee = calculate_tdee(bmr, 1.55)
    bmi = calculate_bmi(70, 175)
    
print(f"BMR: {bmr:.1f} kcal")
print(f"TDEE: {tdee:.1f} kcal")
print(f"BMI: {bmi:.1f} ({classify_bmi(bmi)})")